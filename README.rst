.. image:: https://img.shields.io/pypi/v/jaraco.fabric.svg
   :target: https://pypi.org/project/jaraco.fabric

.. image:: https://img.shields.io/pypi/pyversions/jaraco.fabric.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.fabric/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.fabric

.. image:: https://readthedocs.org/projects/jaracofabric/badge/?version=latest
   :target: https://jaracofabric.readthedocs.io/en/latest/?badge=latest

Fabric tasks and helpers. Includes modules implementing
Fabric tasks.

The easiest way to use jaraco.fabric is to install it and
invoke it using ``python -m jaraco.fabric``. For example,
to list the available commands:

    $ python -m jaraco.fabric -l

Or to install MongoDB 3.2 on "somehost":

    $ python -m jaraco.fabric -H somehost mongodb.distro_install:version=3.2
