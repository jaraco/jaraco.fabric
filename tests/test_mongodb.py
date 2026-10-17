import ast
import getpass
import json
from unittest import mock

import invoke
import pytest

from jaraco.fabric import mongodb


@pytest.fixture
def context():
    return mock.Mock(spec=invoke.Context)


def test_distro_install_unknown_version(context):
    with pytest.raises(RuntimeError, match='Unknown version 4.0'):
        mongodb.distro_install(context, '4.0')


def test_install_user(context, monkeypatch):
    monkeypatch.setenv('USER', 'tester')
    monkeypatch.setattr(getpass, 'getpass', lambda prompt: 'secret')
    mongodb.install_user(context, 'admin')
    (cmd,), _ = context.run.call_args
    prefix = 'mongo admin -eval '
    assert cmd.startswith(prefix)
    script = ast.literal_eval(cmd.removeprefix(prefix))
    doc = json.loads(script.removeprefix('db.createUser(').removesuffix(')'))
    assert doc['user'] == 'admin'
    assert doc['pwd'] == 'secret'
