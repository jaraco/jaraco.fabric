import itertools

flatten = itertools.chain.from_iterable


def install_certs_for(c, *sites):
    cmd = [
        'certbot',
        '--agree-tos',
        '--email',
        'jaraco@jaraco.com',
        '--non-interactive',
        '--nginx',
        'certonly',
    ]
    cmd += list(flatten(['--domain', name] for name in sites))
    c.sudo(' '.join(cmd))
