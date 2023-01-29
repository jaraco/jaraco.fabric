from fabric import task

from . import apt


@task
def install(c, version='3.7'):
    apt.add_ppa('deadsnakes/ppa')
    apt.install_packages(f'python{version}-dev', f'python{version}-venv')
