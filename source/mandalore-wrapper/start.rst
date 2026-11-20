:code:`start` action
====================

This action can be used to start a container. At least one Mandalore image is required to create and start a container and enjoy Mandalore. Installing an image can be done with ``mandalore install`` (documentation
:doc:`here </mandalore-wrapper/install>`).

When this action is used, the following process is applied:

* if no Mandalore image is installed, the user is asked to specify which one to install of build, and the process continues
* then, if the container to start doesn't already exist, it is created based on a Mandalore image and a few settings to specify, and the process continues
* then, the container is started and a shell is opened

.. hint::

    The ``start`` action can be used without any additional argument or option. the wrapper will then enter in an interactive TUI (Text-based User Interface) mode where the user will be asked to choose a few settings.

    .. code-block:: bash

       mandalore start

.. _start_options:

Options
-------

A single option exist to target a Mandalore container.
If this container exists, it will be started if it is not already the case and a shell will be spawned to offer an interactive console to the user

========================= ===============================
 Option                   Description
========================= ===============================
``CONTAINER``             Tag used to target a Mandalore container
========================= ===============================

Many options exist to customize the creation of mandalore container.

.. tip::
    The default options of some commands can be changed in the :ref:`mandalore configuration file<mandalore_configuration>`.

Global options
~~~~~~~~~~~~~~

=========================================================== ===============================
 Option                                                      Description
=========================================================== ===============================
``IMAGE``                                                   Tag of the mandalore image to use to create a new mandalore container
``-w WORKSPACE_PATH``, ``--workspace WORKSPACE_PATH``       The specified host folder will be linked to the /workspace folder in the container.
``-cwd``, ``--cwd-mount``                                   This option is a shortcut to set the /workspace folder to the user's current working directory (pwd).
``-fs``, ``--update-fs``                                    Modifies the permissions of folders and sub-folders shared in your workspace to access the files created within the container using your host user account. (default: Disabled)
``-V VOLUMES``, ``--volume VOLUMES``                        Share a new volume between host and mandalore (format: --volume /path/on/host/:/path/in/container/[:ro|rw]).
``-p PORTS``, ``--port PORTS``                              Share a network port between host and mandalore (format: --port [<host_ipv4>:]<host_port>[:<container_port>][:<protocol>]. This configuration will disable the shared network with the host.
``--hostname HOSTNAME``                                     Set a custom hostname to the mandalore container (default: mandalore-<name>)
``--cap CAP``                                               **(dangerous)** Capabilities allow to add specific privileges to the container (e.g. need to mount volumes, perform low-level operations on the network, etc).
``--privileged``                                            **(dangerous)** Give ALL admin privileges to the container when it is created (if the need is specifically identified, consider adding capabilities instead).
``-d DEVICES``, ``--device DEVICES``                        Add host device(s) at the container creation (example: -d /dev/ttyACM0 -d /dev/bus/usb/).
``--disable-X11``                                           Disable X11 sharing to run GUI-based applications. (default: Enabled)
``--disable-my-resources``                                  Disable the mount of the my-resources (/opt/my-resources) from the host (``~/.mandalore/my-resources`` by default) (default: Enabled)
``--disable-mandalore-resources``                           Disable the mount of the mandalore resources (/opt/resources) from the host (``mandalore_resources_path`` of the configuration) (default: Enabled)
``--disable-shared-network``                                Disable the sharing of the host's network interfaces with mandalore (default: Enabled)
``--disable-shared-timezones``                              Disable the sharing of the host's time and timezone configuration with mandalore (default: Enabled)
``--comment COMMENT``                                       The specified comment will be added to the container info
=========================================================== ===============================

Virtual desktop
~~~~~~~~~~~~~~~

In addition to the X11 sharing functionality, Mandalore can generate its own graphical environment and make it available to the user in a variety of ways.
By default, a web interface gives users access to their own containerized graphical desktop.

========================= ===============================
 Option                   Description
========================= ===============================
``--desktop``             Enable or disable the Mandalore desktop feature (default: Disabled)
``--desktop-config``      Configure your mandalore desktop (vnc or http) and its exposure (format: proto[:ip[:port]]) (default: http:127.0.0.1:<random>)
========================= ===============================

.. _vpn:

VPN
~~~

An additional feature of Mandalore is the VPN tunnel option (OpenVPN).
Just provide an ovpn configuration to mandalore and the container will take care of starting the tunnel at each startup.

========================= ===============================
 Option                   Description
========================= ===============================
``--vpn VPN``             Setup an OpenVPN connection at the container creation (example: --vpn /home/user/vpn/conf.ovpn)
``--vpn-auth VPN_AUTH``   Enter the credentials with a file (first line: username, second line: password) to establish the VPN connection automatically (example: --vpn-auth /home/user/vpn/auth.txt)
========================= ===============================

.. warning::
    All the options seen previously are taken into account **only** for the creation of a **new container**.
    It is **not possible** to modify the configuration of an existing container.
    These options will be **ignored** if a container with the same name already exists.

.. tip::
    A container can still be moved to a newer image while keeping its configuration with :doc:`mandalore upgrade </mandalore-wrapper/upgrade>`.

Shell logging
~~~~~~~~~~~~~

One of the functions of mandalore very useful in a professional context is the shell logging.
This feature allows the user to record **everything** that happens in the mandalore container (commands typed and responses).

=============================== ===============================
 Option                         Description
=============================== ===============================
``-l``, ``--log``               Enable shell logging (commands and outputs) on mandalore to /workspace/logs/ (default: Disabled)
``--log-method``                Select a shell logging method used to record the session (default: ``asciinema``)
``--log-compress``              Enable or disable the automatic compression of log files at the end of the session (default: Enabled)
=============================== ===============================

.. tip::
    When the ``-l``/``--log`` option is enabled during the **creation** of a **new** container, all future shells will be **automatically logged** for this container.

Session specific
~~~~~~~~~~~~~~~~

The options specific to the start of the interactive session

============================================================================================================================== ===============================
 Option                                                                                                                         Description
============================================================================================================================== ===============================
``-e ENVS``, ``--env ENVS``                                                                                                    Add an environment variable on Mandalore (format: --env KEY=value). The variables configured during the creation of the container will be persistent in all shells. If the container already exists, the variable will be present only in the current shell.
``-s SHELL``, ``--shell SHELL`` Select a shell environment to launch at startup: ``zsh``, ``bash`` or ``tmux`` (default: zsh)
============================================================================================================================== ===============================

.. tip::
    The environment variables configured with ``--env ENVS`` during the **creation** of a **new** container will be available to **all** processes of the container during the **entire life cycle** of the container.

Command examples
----------------

.. code-block:: bash

   # Start interactively a container
   mandalore start

   # Create a demo container using full image
   mandalore start demo full

   # Spawn a shell from demo container
   mandalore start demo

   # Create a container test with a custom shared workspace
   mandalore start test full -w "./project/pentest/"

   # Create a container test sharing the current working directory
   mandalore start test full -cwd

   # Create a container htb with a VPN
   mandalore start htb full --vpn "~/vpn/lab_user.ovpn"

   # Create a container app with custom volume
   mandalore start app full -V "/var/app/:/app/"

   # Create a container app with custom volume in read-only
   mandalore start app full -V "/var/app/:/app/:ro"

   # Get a shell based on tmux
   mandalore start --shell tmux

   # Share a specific hardware device (like Proxmark)
   mandalore start -d "/dev/ttyACM0"

   # Share every USB device connected to the host
   mandalore start -d "/dev/bus/usb/"

