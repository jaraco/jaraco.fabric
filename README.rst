jaraco.fabric
=============

Fabric tasks and helpers. Includes modules implementing
Fabric tasks.

The easiest way to use jaraco.fabric is to install it and
invoke it using ``python -m jaraco.fabric``. For example,
to list the available commands:

    $ python -m jaraco.fabric -l

Or to install MongoDB 3.2 on "somehost":

    $ python -m jaraco.fabric -H somehost mongodb.distro_install:version=3.2
