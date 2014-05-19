from fabric.api import sudo, task
from fabric.contrib import files
from fabric.context_managers import settings

from . import apt

@task
def distro_install():
    """
    Install mongodb as an apt package (which also configures it as a
    service).
    """
    content = 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen'
    org_list = '/etc/apt/sources.list.d/mongodb.list'
    files.append(org_list, content, use_sudo=True)
    with settings(warn_only=True):
        sudo('apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10')
    sudo('aptitude update')
    apt.install_packages('mongodb-org')
