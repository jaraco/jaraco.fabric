import sys
import fabric.main


def run_fabric(filename):
    sys.argv.append('--fabfile={filename}'.format(**locals()))
    fabric.main.main()
