:code:`install` action
======================

This action can be used to install a Mandalore image. At least one Mandalore image is required to create and start a container and enjoy Mandalore.

When this action is used, the image can either be:

* **downloaded** (i.e. "pulled" in Docker terms) from `the GitHub Container Registry <https://github.com/ghecko/mandalore/pkgs/container/mandalore>`_ (``ghcr.io/ghecko/mandalore``). In this case, a compressed and pre-built image is downloaded in the form of layers, and then uncompressed. If the registry package is private, run ``docker login ghcr.io`` first (token with the ``read:packages`` scope): the wrapper and docker use the same credentials.
* **built** locally by following the instructions of a Dockerfile offered on `the Mandalore-images GitHub repo <https://github.com/ghecko/mandalore-images>`_. Here again, no need to download the dockerfile manually: the images repository is cloned by the wrapper (``mandalore-images`` submodule for a source installation, ``~/.mandalore/mandalore-images`` otherwise, see ``mandalore_images_path`` in the :ref:`configuration file<mandalore_configuration>`).

.. hint::

    The ``install`` action can be used without any particular argument or option. the wrapper will then enter in an interactive TUI (Text-based User Interface) mode where the user will be asked to choose what image to install or build.

    .. code-block:: bash

       mandalore install

Options
-------

=================== =============
 Option              Description
=================== =============
 ``IMAGE``           Optional positional argument to indicate the image to install (if downloading), or the name of the image to build (if building locally).
 ``BUILD_PROFILE``   Optional positional argument to indicate the source profile to use if building locally.
 ``--build-log``     Write image building logs to the file specified (``LOGFILE_PATH``) if building locally.
 ``--build-path``    Custom path to the dockerfiles and sources (``DOCKERFILES_PATH``).
=================== =============


Command examples
----------------

.. code-block:: bash

   #Install or build interactively a mandalore image
   mandalore install

   #Install or update the full image
   mandalore install full

   #Build interactively a local image named myimage
   mandalore install myimage

   #Build the myimage image based on the full profile and log the operation
   mandalore install myimage full --build-log "/tmp/build.log"