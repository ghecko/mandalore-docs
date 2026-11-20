===================
:code:`stop` action
===================

The purpose of the ``stop`` action is to stop one or more Mandalore containers.

If these containers have a VPN configuration, shutting down the container will cause the VPN tunnel to be disconnected.

Options
=======

The options of the stop action are limited to selecting the container(s) to be stopped.

========================= =============
 Option                    Description
========================= =============
``CONTAINER``             Tag used to target one or more Mandalore containers
``--all``                 Select every Mandalore container
========================= =============


Command examples
================

.. code-block:: bash

    # Stop interactively one or more containers:
    mandalore stop

    # Stop the "demo" container:
    mandalore stop "demo"

    # Stop the "demo", "test" and "dev" container:
    mandalore stop "demo" "test" "dev"

    # Stop every Mandalore container:
    mandalore stop --all
