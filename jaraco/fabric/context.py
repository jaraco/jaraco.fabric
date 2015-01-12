import contextlib

from fabric.api import env

@contextlib.contextmanager
def shell_env(**env_vars):
    """
    A context that updates the shell to add environment variables.
    Ref http://stackoverflow.com/a/8454134/70170
    """
    orig_shell = env['shell']
    env_vars_str = ' '.join(
        '{key}="{value}"'.format(**locals())
        for key, value in env_vars.items()
    )
    env['shell'] = '{env_vars_str} {orig_shell}'.format(**locals())
    try:
        yield
    finally:
        env['shell'] = orig_shell
