=====================
:code:`update` action
=====================

The update process
==================

The mandalore wrapper has an ``update`` action dedicated to updating the different modules (wrapper, resources, etc.) of the project as well as the (docker) Mandalore images.

.. _Modules-updates:

Modules updates
---------------

This action make sure the local copies of the following repositories are up to date:

* `Mandalore <https://github.com/ghecko/mandalore>`_ (wrapper code). If the wrapper has been installed as a package (uv, pipx or pip, not editable), it will not be able to self-update, updating the package will be required (e.g. ``uv tool upgrade mandalore`` or ``pipx upgrade mandalore``).
* `Mandalore-images <https://github.com/ghecko/mandalore-images>`_ (docker building files)
* `Mandalore-resources <https://github.com/ghecko/mandalore-resources>`_ (offline resources, :ref:`mandalore-resources<mandalore-resources>`). This module is optional, and users can choose to install/update it at any time.

.. tip::
    When running ``mandalore update -v``, the user will be able to choose from what branch them module should be synchronized with, allowing to switch easily between release and dev versions.

.. _Images-updates:

Images updates
--------------

Once the local code base is updated, the wrapper compares the installed Mandalore images with those offered on the registry (GHCR). If no parameters have been provided at command-line, an interactive selection will be possible to choose the images to update (if updates are available).

.. hint::
    Older versions of images will be automatically deleted if they are no longer used by any container and if a newer version of the same image is installed.
    This automatic deletion behavior is a default configuration that can be modified in the :ref:`configuration file<mandalore_configuration>` if needed, but it's advised not to change it as disk space is not unlimited and Mandalore image can take up to 30GB.

.. tip::
    Updating an image does not change existing containers: they keep running on the image they were created from. Use :doc:`mandalore upgrade </mandalore-wrapper/upgrade>` to move a container to the newly installed image while keeping its configuration and data.

Options
=======

The options of the ``update`` action are the following.

========================= =============
 Option                   Description
========================= =============
``IMAGE``                 This option specifies what image to update.
``--skip-git``            Skip :ref:`modules updates <Modules-updates>` (wrapper, image sources and mandalore resources).
``--skip-images``         Skip :ref:`images updates <Images-updates>` (mandalore docker images).
========================= =============


Command examples
================

.. code-block:: bash

    # Update interactively a mandalore image:
    mandalore update

    # Update the full image:
    mandalore update full

    # Update the full image without updating mandalore modules:
    mandalore update --skip-git full

    # Update mandalore modules and have the option to change branch without updating docker image:
    mandalore update -v --skip-images
