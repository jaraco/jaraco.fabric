from fabric.api import sudo, task
from fabric.contrib import files
from fabric.context_managers import settings

from . import apt


__all__ = 'distro_install',


APT_KEYS = [
    'EA312927',
]


@task
def distro_install(version):
    """
    Install mongodb as an apt package (which also configures it as a
    service).
    """

    if version.startswith('2.'):
        return distro_install_2(version)

    elif version.startswith('3.'):
        return distro_install_3(version)

    raise RuntimeError('Unknown version {}'.format(version))


def distro_install_2(version):
    """
    Install MongoDB version 2.x
    """
    assert version.startswith('2.')

    # MongoDB 2
    content = (
        'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart '
        'dist 10gen',
    )
    org_list = '/etc/apt/sources.list.d/mongodb.list'
    files.append(org_list, content, use_sudo=True)


def distro_install_3(version):
    """
    Install MongoDB version 3.x
    """
    assert version.startswith('3.')

    lsb_release = apt.lsb_release()
    repo_url = "http://repo.mongodb.org/apt/ubuntu"
    tmpl = "deb {repo_url} {lsb_release}/mongodb-org/{version} multiverse"
    content = tmpl.format(**locals())
    org_list = '/etc/apt/sources.list.d/mongodb-org-{version}.list'.format(**locals())
    files.append(org_list, content, use_sudo=True)

    with settings(warn_only=True):
        for key in APT_KEYS:
            sudo('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv {}'.format(key))

    sudo('aptitude update')
    apt.install_packages('mongodb-org={version}'.format(**locals()))
