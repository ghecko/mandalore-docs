======================
:code:`upgrade` action
======================

The purpose of the ``upgrade`` action is to move one or more existing Mandalore containers to a newer (or another) installed image, while keeping their configuration and the user data that matters.

Docker containers cannot change their image: a container stays on the image it was created from, even after ``mandalore update`` installed a newer version of that image. The ``upgrade`` action recreates the container on the new image for you.

The upgrade process
===================

For each selected container, the wrapper:

#. selects the target image: by default the latest installed version of the container's current image (e.g. ``full``), or the image given with ``--image``.

   * if the registry reports a newer version of this image, the user is offered to :doc:`update </mandalore-wrapper/update>` it first (not in ``--force`` or ``--offline`` mode);
   * if the image is not installed, the user is offered to install it;
   * if the container already uses the latest installed image, nothing is done.

#. shows a recap of what is kept and what is lost, and asks for confirmation (skipped with ``-F``/``--force``).
#. stops the container and renames it to ``<name>-old-<YYYYmmdd-HHMMSS>``.
#. creates a new container with the **same name and configuration** (workspace, volumes, network mode and published ports, devices, capabilities, environment variables, VPN, desktop, shell logging, hostname, etc.) on the target image, then starts it with the usual first-start setup (the image entrypoint loads your :doc:`my-resources </mandalore-image/my-resources>` customizations, as for any new container).
#. transfers the user data that lives **outside** the workspace from the previous container to the new one:

   =============================================== =====================================================================
    Data                                            Transfer method
   =============================================== =====================================================================
   ``/root/.zsh_history``                          merged: the new image history is kept, previous commands are appended
   ``/root/.bash_history``                         merged
   ``/root/.python_history``                       merged
   ``/root/.local/share/hashcat/hashcat.potfile``  merged
   ``/root/.john/john.pot``                        merged
   ``/root/.nxc/workspaces``                       copied (NetExec databases)
   ``/root/.nxc/logs``                             copied
   ``/opt/tools/Responder/Responder.db``           copied
   ``/opt/tools/Responder/logs``                   copied
   ``/etc/hosts``                                  custom entries added to the previous container are appended
   =============================================== =====================================================================

   A path bigger than 1 GiB is skipped (with a warning). A transfer error is reported but does not stop the upgrade.

#. restores the previous state: the new container is stopped again if the previous one was not running.

If anything fails during the creation of the new container (including a ``Ctrl+C``), the new container is removed and the previous container gets its name back (and is restarted if it was running).

.. important::

    The workspace (``/workspace``) and the volumes are shared with the new container, they are never copied nor deleted.

    Everything else modified inside the previous container (packages installed manually, files outside the workspace, volumes and the paths listed above) is **not** carried over. Use the :doc:`my-resources </mandalore-image/my-resources>` feature to make your customizations persistent across containers.

The previous container
======================

By default, the previous container is kept (stopped) under its new name, so that any forgotten data can still be retrieved. Once the new container has been checked, it can be removed with:

.. code-block:: bash

    mandalore remove <name>-old-<YYYYmmdd-HHMMSS>

Removing it does **not** delete the workspace shared with the new container.

With ``--remove-old``, the previous container is removed automatically after a successful upgrade (the workspace is never deleted). If its image is outdated and no longer used, it is removed as well, unless ``auto_remove_image`` is disabled in the :ref:`configuration file<mandalore_configuration>`.

Options
=======

=========================== =============
 Option                     Description
=========================== =============
``CONTAINER``               Tag used to target one or more Mandalore containers
``--all``                   Select every Mandalore container
``-F``, ``--force``         Upgrade container without interactive user confirmation (the image is not updated from the registry).
``--image IMAGE``           Upgrade the container to another installed Mandalore image (default: the container's current image name).
``--remove-old``            Remove the previous container after a successful upgrade instead of keeping it renamed (the workspace is never deleted).
=========================== =============

Command examples
================

.. code-block:: bash

    # Upgrade interactively one or more containers:
    mandalore upgrade

    # Upgrade the "demo" container:
    mandalore upgrade demo

    # Update the full image, then upgrade the "demo" container to it:
    mandalore update full
    mandalore upgrade demo

    # Upgrade every container and remove the previous ones:
    mandalore upgrade --all --remove-old

    # Move the "demo" container to the light image:
    mandalore upgrade demo --image light
