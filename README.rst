.. image:: https://img.shields.io/pypi/v/jaraco.fabric.svg
   :target: https://pypi.org/project/jaraco.fabric

.. image:: https://img.shields.io/pypi/pyversions/jaraco.fabric.svg

.. image:: https://github.com/jaraco/jaraco.fabric/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.fabric/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2023-informational
   :target: https://blog.jaraco.com/skeleton

Fabric tasks and helpers. Includes modules implementing
Fabric tasks.

The easiest way to use jaraco.fabric is to install it and
invoke it using ``python -m jaraco.fabric``. For example,
to list the available commands:

    $ python -m jaraco.fabric -l

Or to install MongoDB 3.2 on "somehost":

    $ python -m jaraco.fabric -H somehost mongodb.distro_install:version=3.2
