=================
Install Mandalore
=================

Installing Mandalore starts with installing the entrypoint to the whole project: the Python wrapper. Once the wrapper is installed, everything else can be managed from it.

.. hint::

   It is strongly advised to install Mandalore on a Linux host, especially when planning on using Mandalore for internal penetration tests. This is because Docker Desktop on Windows and macOS lacks a few features, mainly due to how these operating systems run Docker containers within an internal VM that doesn't share the host's network interfaces and USB accessories.

Once the wrapper is installed, the second step in setting up Mandalore on a device is to install at least one Mandalore image, either with ``mandalore start`` (documentation
:doc:`here </mandalore-wrapper/start>`), or with ``mandalore install`` (documentation
:doc:`here </mandalore-wrapper/install>`). Both actions will guide the user in installing an image if needed.

.. contents::
    :local:

.. _install_requirements:

Requirements
============

The following elements are required before Mandalore can be installed, whatever the host's operating system is:

* git (`Linux <https://github.com/git-guides/install-git#install-git-on-linux>`__ | `macOS <https://github.com/git-guides/install-git#install-git-on-mac>`__ | `Windows <https://github.com/git-guides/install-git#install-git-on-windows>`__)
* python3, version 3.10 or newer (`Linux <https://docs.python.org/3/using/unix.html#on-linux>`__ | `macOS <https://www.python.org/downloads/macos/>`__ | `Windows <https://www.python.org/downloads/windows/>`__)
* docker (`Linux <https://docs.docker.com/engine/install/debian/>`__) or Docker Desktop (`macOS <https://docs.docker.com/desktop/install/mac-install/>`__ | `Windows <https://docs.docker.com/desktop/install/windows-install/>`__)
* at least 100GB of free storage recommended (a minimum of 20GB could be enough, but only for the ``light`` image).

Additional dependencies may be required depending on the host OS.

..  tabs::

    ..  group-tab:: Linux

        No additional dependencies for Linux environments.

        .. tip::

           From Linux systems, Docker can be installed quickly and easily with the following command-line:

           .. code-block:: bash

              curl -fsSL "https://get.docker.com/" | sh

        .. warning::

           By default, ``sudo`` will be required when running docker, hence needed as well for Mandalore. For security reasons, it should stay that way, but it's possible to change that. In order to run mandalore from the user environment without ``sudo``, the user must have the appropriate rights. You can use the following command to grant them to the current user:

           .. code-block:: bash

              # add the sudo group to the user
              sudo usermod -aG docker $(id -u -n)

              # "reload" the user groups with the newly added docker group
              newgrp docker

           For more information, official Docker documentation shows `how to manage docker as a non root user <https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-userm>`_.

        .. warning::

            `Docker "Rootless mode" <https://docs.docker.com/engine/security/rootless/>`_ is not supported by Mandalore as of yet. Please follow the install procedure mentionned above.

    ..  group-tab:: macOS

        To support graphical applications (:ref:`display sharing functionality <feature_x11_sharing>`, e.g. Bloodhound, Wireshark, Burp, etc.), additional dependencies and configuration are required:

        .. hint::

            The XQuartz requirement below is now optional if using the (beta) :ref:`Graphical Remote Desktop feature <feature_desktop>` instead of X11 sharing.

        * `XQuartz <https://www.xquartz.org/>`__ must be installed
        * The XQuartz config ``Allow connections from network clients`` must be set to true
        * Docker Desktop must be configured with default File Sharing (see screenshot below)

        .. figure:: /assets/install/macOS_xquartz_config.png
            :align: center
            :alt: macOS XQuartz configuration requirement

            macOS XQuartz configuration requirement

        .. figure:: /assets/install/macOS_resources_req.png
            :align: center
            :alt: macOS Docker Desktop resources requirement

            macOS Docker Desktop resources requirement

        .. warning::

            You'll also need to add the mandalore source folder (or, more precisely, the folder ``[...]/mandalore/utils/imgsync``).

            If you install Mandalore with uv, pipx or pip, this folder is located where the python packages are installed.
            The path to this folder depends on how you installed python. When creating your first container, you may get an error disclosing the mandalore installation folder, which will have to be added as an authorized resource.

            By default, you can try to add the path: ``/Library/Frameworks/Python.framework`` to the Docker Desktop File sharing allowlist.


        .. tip::

            `OrbStack <https://orbstack.dev/>`__ for **Mac** is supported by Mandalore wrapper from ``v4.2.0``.

            Your mandalore installation cannot be stored under ``/opt`` directory when using OrbStack (`due to OrbStack limitations <https://github.com/orbstack/orbstack/issues/435>`_).

            This support is still in beta, feel free to open issues on `GitHub <https://github.com/ghecko/mandalore/issues/new/choose>`__ if you encounter any bugs.

    ..  group-tab:: Windows

        To support graphical applications (:ref:`display sharing functionality <feature_x11_sharing>`, e.g. Bloodhound, Wireshark, Burp, etc.), additional dependencies and configuration are required:

        * Windows **10** (up to date), or Windows **11**, is required
        * **Docker Desktop** installed on the Windows host
        * Docker Desktop must be configured to run on **WSL2** engine (`how to <https://learn.microsoft.com/en-us/windows/wsl/install>`_)
        * `WSLg <https://github.com/microsoft/wslg#installing-wslg>`_ must be installed to support graphical application
        * at least one WSL distribution must be **installed** as well (e.g. Debian), with **Docker integration** enabled (see screenshot below)


        .. figure:: /assets/install/windows_dockerdesktop_wsl_config.png
            :align: center
            :alt: Windows Docker Desktop WSL integration configuration

            Windows Docker Desktop WSL integration configuration

        In a Windows environment, the Mandalore wrapper can be installed **either** in a **WSL shell** or directly in your Windows environment with **Powershell**.

        .. warning::

            Please note that it is **not** advisable to use Mandalore from both environments at the same time, as this could lead to conflicts and Mandalore does not officially support this configuration.

        .. warning::

            You may want to disable Windows Defender during the installation, as Mandalore will download pre-built remote shells (or temporarily exclude ``C:\Users\<username>\AppData\Local\Temp`` or the source file directory).

            You should also add the folder ``C:\Users\<user>\.mandalore\mandalore-resources`` to the exclusion list.


.. _mandalore_install:

Installation
============

The installation of Mandalore on Linux, macOS and Windows are very similar. The wrapper requires **Python 3.10 or newer**. It is installed from its GitHub repository, either as an isolated tool (with ``uv`` or ``pipx``) or used directly from a git clone (fully featured, with self-update).

.. note::

   Mandalore is not published on PyPI (yet). The commands below install it from GitHub.


1. Installation of mandalore
----------------------------

..  tabs::
    ..  group-tab:: Installing with uv / pipx (preferred)

        Installing with `uv <https://docs.astral.sh/uv/>`__ or `pipx <https://pipx.pypa.io/>`__ puts Mandalore in an **isolated** virtual environment **dedicated** to it.

        .. code-block:: bash

            # with uv
            uv tool install "git+https://github.com/ghecko/mandalore"

            # OR with pipx (install pipx first if needed: sudo apt install pipx)
            pipx install "git+https://github.com/ghecko/mandalore"

        With this installation mode, the mandalore images and resources repositories are cloned on demand in ``~/.mandalore/``.

    ..  group-tab:: Installing from sources

        Mandalore's wrapper can be used from a git clone. The wrapper then knows how to self-update, and switching from release and development branches is possible and very easy. The images and resources repositories are git submodules of the wrapper repository.

        .. code-block:: bash

            git clone --recurse-submodules "https://github.com/ghecko/mandalore"

        The clone can then be installed as an editable tool (recommended, the ``mandalore`` command stays in sync with the clone):

        .. code-block:: bash

            uv tool install --editable ./mandalore
            # OR
            pipx install --editable ./mandalore

        Alternatively, install the requirements and run ``mandalore.py`` directly. If you have access to docker directly as a user, you can install the requirements only for your current user, otherwise the requirements must be installed as root to run Mandalore with sudo.

        .. tabs::

           .. tab:: With sudo

               .. code-block:: bash

                  sudo python3 -m pip install --requirement "mandalore/requirements.txt"

           .. tab:: Directly as user

               .. code-block:: bash

                  python3 -m pip install --user --requirement "mandalore/requirements.txt"

        .. warning::

            In some cases, it is no longer possible to add a pip package system-wide (PEP 668). In such cases, prefer the ``uv tool`` / ``pipx`` installation.


2. Adding Mandalore to the ``PATH``
-----------------------------------

..  tabs::

    ..  group-tab:: Installing with uv / pipx (preferred)

        In order to use uv or pipx applications, their bin directory must be set in your PATH:

        .. code-block:: bash

            uv tool update-shell
            # OR
            pipx ensurepath

        Dont forget to open a **new terminal** to reload your PATH before continuing.

    ..  group-tab:: Installing from sources

        If the clone was installed with ``uv tool install --editable`` or ``pipx install --editable``, follow the uv / pipx tab. Otherwise:

        ..  tabs::
            .. tab:: Linux & MacOS

                The mandalore wrapper can be added to the ``PATH`` with a symlink for direct access. This allows to call mandalore from wherever, instead of using the absolute path. Mandalore can then be used with ``mandalore <action>`` instead of ``python3 /path/to/mandalore/mandalore.py <action>``.

                .. code-block:: bash

                   sudo ln -s "$(pwd)/mandalore/mandalore.py" "/usr/local/bin/mandalore"

            ..  group-tab:: Windows

                The mandalore wrapper can be added as a PowerShell command alias. Mandalore can then be used with ``mandalore <action>`` instead of ``python3 /path/to/mandalore/mandalore.py <action>``.

                To create the alias file correctly, open a PowerShell and place yourself in the folder where mandalore is located and run the following commands:

                Create `$PROFILE` file if it doesn't exist:

                .. code-block:: powershell

                    if (!(Test-Path -Path $PROFILE)) {
                        New-Item -ItemType File -Path $PROFILE -Force
                    }

                Create alias for Mandalore in `$PROFILE`:

                .. code-block:: powershell

                    echo "Set-Alias -Name mandalore -Value '$(pwd)\mandalore.py'" >> $PROFILE

                .. warning::

                   To automatically load aliases from the ``.ps1`` file, PowerShell's ``Get-ExecutionPolicy`` must be set to ``RemoteSigned``.

                   If the configuration is not correct it can be configured as **administrator** with the following command:

                   .. code-block:: powershell

                      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

                .. tip::
                    If you have installed Python3 manually and Windows opens the **Microsoft store** on the python page as soon as you type ``python3.exe``, try this:

                    It is possible to disable this behavior in the Windows settings: ``Apps > Apps & features > App execution aliases`` and disable aliases for ``python.exe`` and ``python3.exe``.

.. _install_mandalore_privileges:

3. Run Mandalore with appropriate privileges
--------------------------------------------


..  tabs::

    ..  group-tab:: Linux

        Mandalore does not support rootless docker. To interact with docker, you must either have your user be a member of the docker group to use mandalore as a user, or run Mandalore with root privileges using sudo.

        ..  tabs::

            .. tab:: Run as root (preferred)

                To run Mandalore as root with sudo, you must use a specific sudo command. For a better user experience, we recommend using an alias:

                ..  tabs::

                    .. group-tab:: Bash

                        .. code-block:: bash

                            echo "alias mandalore='sudo -E $(which mandalore)'" >> ~/.bash_aliases
                            source ~/.bashrc

                    .. group-tab:: Zsh

                        .. code-block:: bash

                            echo "alias mandalore='sudo -E $(which mandalore)'" >> ~/.zshrc
                            source ~/.zshrc

                    .. tip::distribution

                        Please note that on most Linux distros, .bash_aliases is included in .bashrc. However, this is not the case in some distributions (i.e. Arch Linux). If this is your case, it is recommended to include .bash_aliases in .bashrc by adding these lines in your .bashrc file (for more details, please follow the documentation of your Linux distribution): 

                        .. code-block:: bash

                            if [ -f ~/.bash_aliases ]; then
                                . ~/.bash_aliases
                            fi

            .. tab:: Run as user

                .. warning::

                    By giving the user direct access to docker, this allows the user to compromise the host and become **root** on the machine with full access to the file system.

                    For more information, official Docker documentation shows `how to manage docker as a non root user <https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-userm>`_.

                If you accept this risk because the environment is not critical and you prefer ease of use without the security control provided by sudo, you can apply the following method to use mandalore directly as a user:

               .. code-block:: bash

                    # add the sudo group to the user
                    sudo usermod -aG docker $(id -u -n)

                    # To apply the new group you must open a new shell
                    exit
                    # OR "reload" the user groups with the newly added docker group
                    newgrp docker

    ..  group-tab:: macOS

        Mandalore should **NOT** be used as root on macOS. Docker Desktop (or Orbstack) do not require root privileges.

    ..  group-tab:: Windows

        Mandalore should **NOT** be used as admin on Windows and **NOT** as root in a WSL instance. Docker Desktop doesn't require administrator privileges.


4. Installation of the first Mandalore image
--------------------------------------------

Once the mandalore wrapper is installed, you can download your first docker image with the following command:

.. code-block:: bash

   mandalore install

Images are pulled from the GitHub Container Registry (``ghcr.io/ghecko/mandalore``). If the package is not public, log in first with a GitHub token that has the ``read:packages`` scope; the wrapper reuses your Docker credentials:

.. code-block:: bash

   docker login ghcr.io


5. (Optional) Using Mandalore auto-completion
---------------------------------------------

Mandalore (wrapper) supports auto-completion in many shell environments but there is a configuration to add (on the host) for this feature to work.

.. important::

    The following configurations must be made in your **host** environment.

.. tip::

    If the command ``register-python-argcomplete`` is not found on your host, you have to install it:

    .. code-block:: bash

        # Using the system package manager
        sudo apt install python3-argcomplete

        # Or using pip (check if pip packages are included in your $PATH)
        pip3 install --user argcomplete

        # Or using pipx (check if pipx packages are included in your $PATH)
        pipx install argcomplete

..  tabs::
    ..  tabs::
        .. group-tab:: Bash

            You can enable Mandalore auto-completion for your **current user** with your ``.bashrc`` or you can enable the auto-completion **system-wide** with ``bash-completion``.

            ..  tabs::

                .. tab:: Via bash-completion

                    To setup the auto-completion system-wide you first need to install ``bash-completion`` on your system (if not already installed).

                    .. code-block:: bash

                        sudo apt update && sudo apt install bash-completion

                    At this point you should have a ``/etc/bash_completion.d/`` folder. It's in there that you can add any auto-completion module that you want.

                    To generate and install the mandalore completion configuration you can execute the following command with ``register-python-argcomplete``:

                    .. code-block:: bash

                        register-python-argcomplete --no-defaults mandalore | sudo tee /etc/bash_completion.d/mandalore > /dev/null

                .. tab:: Via .bashrc

                    Add the following command in your ``~/.bashrc`` config:

                    .. code-block:: bash

                        eval "$(register-python-argcomplete --no-defaults mandalore)"


            .. tip::
                If you have multiple tools using ``argcomplete`` you can also use the `global completion <https://kislyuk.github.io/argcomplete/#global-completion>`__ method (need bash >= 4.2).

        .. group-tab:: Zsh

            To activate completions for zsh you need to have ``compinit`` enabled in zsh:

            .. code-block:: bash

                autoload -U compinit
                compinit

            Afterwards you can enable completion by adding the following command in your ``~/.zshrc`` config:

            .. code-block:: bash

                eval "$(register-python-argcomplete --no-defaults mandalore)"

        .. group-tab:: Fish

            To activate completions for fish use:

            .. code-block:: bash

                register-python-argcomplete --no-defaults --shell fish mandalore | source

            or create new completion file, e.g:

            .. code-block:: bash

                register-python-argcomplete --no-defaults --shell fish mandalore > ~/.config/fish/completions/mandalore.fish

        .. group-tab:: Tcsh

            To activate completions for tcsh use:

            .. code-block:: bash

                eval `register-python-argcomplete --no-defaults --shell tcsh mandalore`

        .. tab:: PowerShell

            To activate completions for PowerShell, first generate completion file :

            .. code-block:: powershell

                register-python-argcomplete --no-defaults --shell powershell mandalore > $HOME\Documents\WindowsPowerShell\mandalore_completion.psm1

            .. warning::

                If the command ``register-python-argcomplete`` is not found, that means that python pip script are not in your PATH.
                You can ty to fix your pip installation: `Linux <https://stackoverflow.com/a/62823029>`__ | `MacOS <https://stackoverflow.com/a/43368894>`__ | `Windows <https://builtin.com/software-engineering-perspectives/pip-command-not-found>`__
                Or find the direct Python script path, it might be something like:  ``$HOME\AppData\Roaming\Python\Python311\Scripts\register-python-argcomplete`` (``Python311`` PATH depends on the version of Python you have installed, it must be updated to match your local setup).
            
            Then import this completion file in `$PROFILE`:

            .. code-block:: powershell

                echo "Import-Module '$HOME\Documents\WindowsPowerShell\mandalore_completion.psm1'" >> $PROFILE
            
            .. tip::
                
                You can have Zsh style completion in PowerShell using this:

                .. code-block:: powershell

                    echo "Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete" >> $PROFILE
