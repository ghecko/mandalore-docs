=====================
:code:`remove` action
=====================

The purpose of the ``remove`` action is to remove one or more Mandalore container.

If the deleted container was using an outdated image, the wrapper will (by default) try to delete that outdated image automatically (unless this default behavior is changed in the :ref:`mandalore configuration file<mandalore_configuration>`, which is not advised since disk space is not limited and Mandalore images can take up to 30GB). The disk space used by each container and its workspace can be checked beforehand with :doc:`info </mandalore-wrapper/info>`.

When deleting the container, the wrapper will check if the content of the ``/workspace`` volume is empty. If the workspace is **empty**, mandalore will **automatically delete** the folder on the host, otherwise it will **explicitly ask the user** if the workspace content should be **deleted** or not.

Options
=======

The options of the ``remove`` action are limited to selecting the container(s) to be removed and forcing the removal without asking the user for interactive confirmation.

========================= =============
 Option                    Description
========================= =============
``CONTAINER``             Tag used to target one or more Mandalore containers
``--all``                 Select every Mandalore container
``-F``, ``--force``       Remove container without interactive user confirmation (confirmation will still be required for removing non-empty workspaces).
========================= =============


Command examples
================

.. code-block:: bash

    # Remove interactively one or more containers:
    mandalore remove

    # Remove the "demo" container:
    mandalore remove "demo"

    # Remove the "demo", "test" and "dev" container without asking for user confirmation:
    mandalore remove -F "demo" "test" "dev"

    # Remove every Mandalore container:
    mandalore remove --all
