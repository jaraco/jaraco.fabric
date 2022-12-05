import functools


def workaround_2090(func):
    """
    Wrap a task func to work around fabric/fabric#2090.
    """

    @functools.wraps(func)
    def wrapper(c, *args, **kwargs):
        c.connect_kwargs['key_filename'][:] = [
            key
            for key in c.connect_kwargs['key_filename']
            if __import__('os').path.exists(key)
        ]
        return func(c, *args, **kwargs)

    return wrapper
