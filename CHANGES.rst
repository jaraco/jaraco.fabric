4.1
===

Refreshed package.

4.0
===

Added Python module.

Dropped support for Python 3.5 and earlier.

3.5
===

Added more tasks for supporting MongoDB deployment:

 - enable_authentication
 - install_user
 - bind_all

3.4
===

* #3: Fix version handling for both repo selection and
  package installation on MongoDB. Set default version
  to 3.2. Now one can simply install the major release
  as so:

    python -m jaraco.fabric mongodb.distro_install:3.2

  Or install the default version with no version at all:

    python -m jaraco.fabric mongodb.distro_install

* #4: Install the systemd configuration so that the
  service is managed.

3.3
===

Prefer ``apt`` to ``aptitude``.

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
