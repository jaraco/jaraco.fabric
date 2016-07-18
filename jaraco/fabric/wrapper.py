import sys
import fabric.main
import pkg_resources


def run_fabric():
    filename = pkg_resources.resource_filename('jaraco.fabric', 'fabfile.py')
    sys.argv.append('--fabfile={filename}'.format(**locals()))
    fabric.main.main()
