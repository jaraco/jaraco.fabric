v6.0.0
======

Updated API to work with fabric 2 instead of Fabric 3. Most
behaviors untested and likely broken, but tests run and pass.

v5.3.0
======

Added ``monkey`` module.

v5.2.1
======

Fixed ``context`` parameter of ``upload_template``.

v5.2.0
======

Added files routines.

v5.1.0
======

Package refresh.

5.0
===

Switch to `pkgutil namespace technique
<https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages>`_
for the ``jaraco`` namespace.

4.1.1
=====

Fixed issue where ``apt.add_ppa`` would fail if the PPA
was already present. Better to be idempotent.

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
