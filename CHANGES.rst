3.2
===

Allow package to be executed with ``-m jaraco.fabric``,
creating a fabfile and running Fabric against it.

Package is automatically deployed via continuous
integration when tests pass on Python 3.

3.1
===

Move hosting to Github.

3.0
===

MongoDB distro_install command now requires a version
be specified as to which version to install. Invoke
with

    fab distro_install:3.2

or similar.

2.0
===

Removed jaraco.fabric.context, obviated by Fabric 1.5.

1.0
===

Initial release with Apt support.
