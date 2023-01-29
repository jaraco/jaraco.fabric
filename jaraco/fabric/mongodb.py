import os
import re
import json
import getpass
import contextlib
import io

import pkg_resources
import yaml
from fabric import task

from . import apt


__all__ = (
    'distro_install',
    'find_current_version',
    'install_systemd',
    'enable_authentication',
    'install_user',
    'bind_all',
)


APT_KEYS = ['EA312927']


@task
def distro_install(c, version="3.2"):
    """
    Install mongodb as an apt package (which also configures it as a
    service).
    """

    if version.startswith('2.'):
        return distro_install_2(version)

    elif version.startswith('3.'):
        return distro_install_3(version)

    raise RuntimeError('Unknown version {}'.format(version))


def append(c, *args, **kwargs):
    # todo: used to be contrib.files.append, now patchwork.files, not ported
    raise NotImplementedError()


def distro_install_2(c, version):
    """
    Install MongoDB version 2.x
    """
    assert version.startswith('2.')

    # MongoDB 2
    content = (
        'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart ' 'dist 10gen',
    )
    org_list = '/etc/apt/sources.list.d/mongodb.list'

    append(c, org_list, content, use_sudo=True)


@task
def find_current_version(c):
    output = c.sudo('apt list -qq mongodb-org')
    return re.search(r'\d+\.\d+\.\d+', output).group(0)


def distro_install_3(c, version):
    """
    Install MongoDB version 3.x
    """
    assert version.startswith('3.')

    lsb_release = apt.lsb_release()
    repo_url = "http://repo.mongodb.org/apt/ubuntu"
    tmpl = "deb {repo_url} {lsb_release}/mongodb-org/{version} multiverse"
    content = tmpl.format(**locals())
    org_list = f'/etc/apt/sources.list.d/mongodb-org-{version}.list'
    append(c, org_list, content, use_sudo=True)

    for key in APT_KEYS:
        c.sudo(
            'apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 ' f'--recv {key}',
            warn=True,
        )

    c.sudo('apt update')
    version = find_current_version()
    apt.install_packages('mongodb-org={version}'.format(**locals()))
    install_systemd()


@task
def enable_authentication(c):
    with yaml_config(c, '/etc/mongod.conf', use_sudo=True) as config:
        security = config.setdefault('security', {})
        security['authorization'] = 'enabled'


@task
def bind_all(c):
    """
    Bind to all interfaces.
    """
    with yaml_config('/etc/mongod.conf', use_sudo=True) as config:
        config.setdefault('net', {}).update(bindIp='0.0.0.0')


@contextlib.contextmanager
def yaml_config(c, path, use_sudo=False):
    cmd = c.sudo if use_sudo else c.run
    doc = yaml.safe_load(cmd('cat {path}'.format(**locals())))
    yield doc
    new_doc = io.StringIO(yaml.dump(doc, default_flow_style=False))
    c.put(new_doc, path, use_sudo=use_sudo)


@task
def install_user(c, username=None):
    default = os.environ['USER']
    username = username or getpass.getuser()
    password = getpass.getpass('password> ')
    new_user = dict(
        user=username,
        pwd=password,
        roles=[dict(role="userAdminAnyDatabase", db="admin")],
    )
    cmd = 'db.createUser({doc})'.format(doc=json.dumps(new_user))
    c.run('mongo admin -eval {cmd!r}'.format(**locals()))


@task
def install_systemd(c):
    """
    On newer versions of Ubuntu, make sure that systemd is configured
    to manage the service.
    https://docs.mongodb.com/v3.2/tutorial/install-mongodb-on-ubuntu/#ubuntu-16-04-only-create-systemd-service-file
    """
    if apt.lsb_version() < '15.04':
        return

    fn = 'mongod.service'
    service_strm = pkg_resources.resource_stream(__name__, fn)
    c.put(service_strm, '/lib/systemd/system/' + fn, use_sudo=True)
    c.sudo('systemctl enable mongod')
    # TODO: does the service start automatically? If not,
    # sudo('systemctl start mongod')
