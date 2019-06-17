import pkg_resources

from . import wrapper


if __name__ == '__main__':
    filename = pkg_resources.resource_filename(__name__, 'fabfile.py')
    wrapper.run_fabric(filename)
