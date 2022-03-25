"""
Fabric 2 implementations of file routines that
used to come with Fabric 1.
"""

import tempfile
import pathlib
import io


def is_dir(c, candidate):
    cmd = f'test -d "{candidate}"'
    return c.run(cmd, warn=True)


def exists(c, candidate):
    cmd = f'test -f "{candidate}"'
    return c.run(cmd, warn=True)


def upload_template(c, src, dest, *, mode=None, context={}):
    rnd_name = next(tempfile._get_candidate_names())
    tmp_dest = f'/tmp/{rnd_name}'
    template = pathlib.Path(src).read_text()
    content = template % context
    stream = io.StringIO(content)
    c.put(stream, tmp_dest)
    if is_dir(c, dest):
        dest = pathlib.PurePosixPath(dest, pathlib.Path(src).name)
    c.sudo(f'mv "{tmp_dest}" "{dest}"')
    if mode is not None:
        mode_str = oct(mode)[2:]
        c.run(f'chmod {mode_str} {dest}')
