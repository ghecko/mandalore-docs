======================
:code:`restart` action
======================

The purpose of the ``restart`` action is to stop and directly restart a Mandalore container.

If these containers have a ``privileged`` or ``device`` configuration, restarting the container will refresh the available devices inside the container.

.. warning::

    Restarting a container will reset the ``hosts``, ``resolv.conf`` files (and probably more).

Options
=======

The options of the restart action are limited to selecting the container to be restarted and some starting options that can be also found on the :ref:`start action<start_options>`.

========================= =============
 Option                   Description
========================= =============
``CONTAINER``             Tag used to target the Mandalore container to restart
``-l``, ``--log``         Enable shell logging (commands and outputs) on mandalore to /workspace/logs/ (default: Disabled)
``--log-method``          Select a shell logging method used to record the session: ``asciinema`` or ``script`` (default: asciinema)
``--log-compress``        Enable or disable the automatic compression of log files at the end of the session (default: Enabled)
``-e``, ``--env ENVS``    Add an environment variable to the shell spawned after the restart (format: --env KEY=value)
``-s``, ``--shell``       Select a shell environment to launch at startup: ``zsh``, ``bash`` or ``tmux`` (Default: zsh)
========================= =============


Command examples
================

.. code-block:: bash

    # Restart interactively one container:
    mandalore restart

    # Restart the "demo" container:
    mandalore restart "demo"
