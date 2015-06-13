from __future__ import print_function

import io
import re
import contextlib

import jaraco.apt
from jaraco.itertools import always_iterable
from fabric.operations import sudo, run
from fabric.api import task, put
from fabric.context_managers import settings
import fabric.utils

@contextlib.contextmanager
def package_context(target, action='install'):
    """
    A context for installing the build dependencies for a given target (or
    targets). Uses aptitude. Removes the dependencies when the context is
    exited. One may prevent the removal of some or all packages by modifying
    the list within the context.
    """
    target = ' '.join(always_iterable(target))
    status = sudo('aptitude {action} -q -y {target}'.format(**vars()))
    packages = jaraco.apt.parse_new_packages(status)
    try:
        yield packages
    finally:
        remove_packages(packages)

@task
def install_packages(*packages):
    with package_context(packages) as to_remove:
        installed = list(to_remove)
        to_remove[:] = []
    return installed

def build_dependency_context(target):
    return package_context(target, 'build-dep')

def remove_packages(packages):
    if not packages:
        print("No packages specified, nothing to remove")
        return
    sudo('aptitude remove -y -q ' + ' '.join(packages))

@task
def create_installers_group():
    """
    Create an 'installers' group that has rights to install/remove software
    without typing a password.
    """
    apt_commands = ['aptitude', 'apt-get', 'dpkg', 'apt-key',
            'apt-add-repository', 'apt-cache']
    commands = ', '.join('/usr/bin/' + cmd for cmd in apt_commands)
    content = "%installers ALL=NOPASSWD: {commands}\n".format(**locals())
    upload_sudoersd_file('installers', content)
    with settings(warn_only=True):
        sudo('addgroup installers')
    print("Grant installation privilege with 'usermod -a -G installers $username' or yg-fab add_installer:$username")

def upload_sudoersd_file(name, content):
    """
    Thanks to a long-standing bug in Ubuntu Lucid
    (https://bugs.launchpad.net/ubuntu/+source/sudo/+bug/553786),
    we have to take special precaution when creating sudoers.d files.
    """
    stream = io.BytesIO(content.encode('utf-8'))
    tmp_name = '/tmp/'+ name
    put(stream, tmp_name, mode=0o440)
    sudo('chown root:root ' + tmp_name)
    sudo('mv {tmp_name} /etc/sudoers.d'.format(**vars()))

@task
def add_installer(username):
    """
    Add username to the installers group, after which they should be able to
    install/remove software without typing a password.
    """
    sudo("usermod -a -G installers {username}".format(**vars()))

def ubuntu_version():
    pattern = re.compile('Ubuntu ([\d.]+)')
    out = run('cat /etc/issue')
    return pattern.match(out).group(1)

@task
def add_ppa(name):
    """
    Add the Personal Package Archive
    """
    sudo('aptitude update')
    # need python-software-properties for apt-add-repository
    sudo('aptitude install -q -y python-software-properties')
    # apt-add-repository returns 0 even when it failed, so check its output
    #  for success or failure.
    cmd = [
        'apt-add-repository',
        'ppa:' + name,
    ]
    if ubuntu_version() >= '12.':
        cmd[1:1] = ['-y']
    res = sudo(' '.join(cmd))
    if not 'Total number processed: 1' in res:
        msg = "Failed to add PPA {name}".format(**vars())
        fabric.utils.abort(msg)
    sudo('aptitude update')
