from fabric.api import task

from . import apt


@task
def install(version='3.6'):
	apt.add_ppa('deadsnakes/ppa')
	apt.install_packages(f'python{version}-dev', f'python{version}-venv')
