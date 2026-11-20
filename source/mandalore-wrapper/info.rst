===================
:code:`info` action
===================

The ``info`` action aims at displaying all the information specific to the Mandalore project on the current system.
This action can also be used by targeting a specific container to display its configuration in detail.

Depending on the verbosity level specified in the command-line, the information displayed will be more or less detailed accordingly.

.. tabs::

    .. tab:: Standard (default)

        .. code-block:: bash

            mandalore info

        * List of available Mandalore Images

            * Name of the image
            * Size of each image (disk space if the image is installed, otherwise its compressed size to download for installation)
            * Status of each image

                * Not installed (Image available for download from the registry)
                * Up to date (The latest version of the image is installed and ready to be used)
                * Update available (A new version is available for download on the registry)
                * Outdated (Old version of an image that has been updated since)
                * Local image (Locally built image)
                * Discontinued (if your image is no longer available on the registry)
                * Unknown (the registry could not be reached, or the package is private and ``docker login ghcr.io`` has not been done)

        * List of Mandalore Containers

            * Name of each container
            * Container status (Stopped or running)
            * Image name (Mandalore image used as a base to create the container)
            * Configurations (Display of non-default configurations)

    .. tab:: Verbose

        .. code-block:: bash

            mandalore info -v

        In the verbose mode, the following additional elements are displayed. Everything from the lower verbosity level is still displayed.

        * Enumerate every user configuration (see details :ref:`here<mandalore_configuration>`)

        * In the list of available Mandalore Images

            * Image ID
            * Build date
            * Image architecture (AMD64 / ARM64)

        * In the list of Mandalore Containers

            * Container id
            * Size: disk space used by the container's writable layer (files created or modified inside the container, outside of volumes)
            * Full configuration
            * List of non-technical volumes
            * List of Devices
            * List of Ports (Applicable if network sharing with host is not enabled)
            * List of custom environment variables

    .. tab:: Advanced

        .. code-block::

            mandalore info -vv

        In the advanced mode, the following additional elements are displayed. Everything from the lower verbosity levels is still displayed.

        * Enumerate the settings from the user configuration at ``~/.mandalore/config.yml`` (see details :ref:`here<mandalore_configuration>`)

        * List the different mandalore modules

            * Modules name
            * Their update status
            * Their git branch (if applicable)

    .. tab:: Debug

        .. code-block::

            mandalore info -vvv

        In the debug mode, everything from the lower verbosity levels is still displayed, as well as logs from internal methods and functions. Those logs can be useful for maintainers and developers in case of bug, or for making sure everything works properly.


Options
=======

The info action does not have many parameters, its use is relatively simple. This action can either be used to gather general information (available images, containers, user configs, etc.), or gather information about a specific container and display its configuration.

========================= =============
 Option                   Description
========================= =============
``CONTAINER``             Optional positional argument to indicate the container tag of which to display the configuration.
========================= =============

When a container is targeted, its recap includes a **Disk usage** row: the disk space used by the container itself (writable layer) and, in verbose mode (``-v``), the size of its workspace on the host.

Global options can still be used, like for any action.

========================= =============
 Option                   Description
========================= =============
``-h``, ``--help``        Show the help message of any action
``-v``, ``--verbose``     Verbosity level (-v for verbose, -vv for advanced, -vvv for debug)
``-q``, ``--quiet``       Show no information at all
``-k``, ``--insecure``    Allow insecure server connections for web requests, e.g. when fetching info from the registry (default: Secure)
``--offline``             Run mandalore in offline mode, no request will be made on internet (default: Disable)
``--arch {arm64,amd64}``  Overwrite default image architecture (default: host's arch)
========================= =============

Command examples
================

.. code-block:: bash

    # Print containers and images essentials information:
    mandalore info

    # Print the detailed configuration of the "demo" container:
    mandalore info demo

    # Print verbose information:
    mandalore info -v

    # Print advanced information:
    mandalore info -vv

    # Print debug information:
    mandalore info -vvv
