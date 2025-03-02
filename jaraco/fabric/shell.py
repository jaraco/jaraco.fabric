import functools


@functools.cache
def get_shell(c):
    return c.run('echo $SHELL', hide=True).stdout


def escape_param(c, param):
    """
    Some parameters need shell-specific escaping.
    """
    shell = get_shell(c)
    if 'xonsh' in shell:
        return repr(param)
    return f"'{param}'"
