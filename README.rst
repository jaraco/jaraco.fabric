.. image:: https://img.shields.io/pypi/v/jaraco.fabric.svg
   :target: https://pypi.org/project/jaraco.fabric

.. image:: https://img.shields.io/pypi/pyversions/jaraco.fabric.svg

.. image:: https://img.shields.io/pypi/dm/jaraco.fabric.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.fabric/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.fabric


License
=======

License is indicated in the project metadata (typically one or more
of the Trove classifiers). For more details, see `this explanation
<https://github.com/jaraco/skeleton/issues/1>`_.

Docs
====

There's `no good mechanism for publishing documentation
<https://github.com/pypa/python-packaging-user-guide/pull/266>`_
easily. If there's a documentation link above, it's probably
stale because PyPI-based documentation is deprecated. This
project may have documentation published at ReadTheDocs, but
probably not. Good luck finding it.

Fabric tasks and helpers. Includes modules implementing
Fabric tasks.

The easiest way to use jaraco.fabric is to install it and
invoke it using ``python -m jaraco.fabric``. For example,
to list the available commands:

    $ python -m jaraco.fabric -l

Or to install MongoDB 3.2 on "somehost":

    $ python -m jaraco.fabric -H somehost mongodb.distro_install:version=3.2
