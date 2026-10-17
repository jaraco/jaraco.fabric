from importlib_resources import as_file, files

from . import wrapper

if __name__ == '__main__':
    with as_file(files(__package__) / 'fabfile.py') as filename:
        wrapper.run_fabric(filename)
