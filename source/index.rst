.. Mandalore documentation master index file

=====================================
Mandalore: professional hacking setup
=====================================

.. raw:: html

    <div align="center">
      <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10+-informational">
      <img alt="Licence GPLv3" src="https://img.shields.io/badge/licence-GPLv3-informational">
      <br>
      <img alt="linux" src="https://img.shields.io/badge/linux-supported-success">
      <img alt="windows" src="https://img.shields.io/badge/windows-supported-success">
      <img alt="mac" src="https://img.shields.io/badge/mac-supported-success">
      <br>
      <img alt="amd64" src="https://img.shields.io/badge/amd64%20(x86__64)-supported-success">
      <img alt="arm64" src="https://img.shields.io/badge/arm64%20(aarch64)-supported-success">
      <br><br>
    </div>

Mandalore is a community-driven hacking environment, powerful and yet simple enough to be used by anyone in day to day engagements. Mandalore is the best solution to deploy powerful hacking environments securely, easily, professionally. No more unstable, not-so-security-focused systems lacking major offensive tools. Kali Linux (and similar alternatives) are great toolboxes for learners, students and junior pentesters. But professionals have different needs, and their context require a whole new design.

Mandalore fits pentesters, CTF players, bug bounty hunters, researchers, beginners and advanced users, defenders, from stylish macOS users and corporate Windows pros to UNIX-like power users.

.. note::

   Mandalore is a fork of `Exegol <https://github.com/ThePorgs/Exegol>`_, started from Exegol **4.3.12**, the GPLv3 code base, before the licence change of Exegol 5. Mandalore stays free and open-source (GPLv3). All credits for the original project go to the Exegol authors and contributors. See :doc:`About Mandalore </the-mandalore-project/about>`.

.. warning::

   This documentation is a work in progress. If there are things you'd like to be documented in priority, feel free to open an issue on the `GitHub repo <https://github.com/ghecko/mandalore-docs/issues>`_.

The Mandalore project
---------------------

Mandalore is many things in one. Try it, and you'll stop using your old, unstable and risky environment, no more monolithic system that gets messier, buggier and more at risk with time.

* :doc:`Python wrapper </the-mandalore-project/python-wrapper>`: makes everyone's life easier. This entrypoint to the whole Mandalore project handles all docker and git operations so you don't have to. **Now's the time to have a clean environment** with one Docker container per engagement without the effort. Mandalore handles multiple images and multiple containers. GUI apps, Wi-Fi, USB accessories, volume mounting and many more features are supported and easier to use than ever.
* :doc:`Docker images </the-mandalore-project/docker-images>`: a set of pre-built docker images and dockerfiles that include a neat choice of tools, zsh plugins for power users, pre-filled history ready to use with environment variables, awesome resources, custom configs and many more. Images can either be built locally or pulled from the GitHub Container Registry (``ghcr.io/ghecko/mandalore``).
* :doc:`Offline resources </the-mandalore-project/offline-resources>`: Tired of always having to search github for your favorite privesc enumeration script? Mandalore includes a set of resources, shared with all mandalore containers and your host, including LinPEAS, WinPEAS, LinEnum, PrivescCheck, SysinternalsSuite, mimikatz, Rubeus, PowerSploit and many more.

Getting started
---------------

Wanna try Mandalore? You need to :ref:`install requirements <install_requirements>` first, then proceed to the OS-specific instructions: :ref:`Linux<mandalore_install>` | :ref:`macOS<mandalore_install>` | :ref:`Windows<mandalore_install>`

Community
---------

Have a bug report or feature request? Open an issue on the `Mandalore repo`_ (see :doc:`where to open an issue </community/users>`).

.. _Mandalore repo: https://github.com/ghecko/mandalore

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting started

   getting-started/install.rst
   getting-started/troubleshooting.rst
   getting-started/updates.rst
   getting-started/faq.rst
   getting-started/tips-and-tricks.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: The Mandalore Project

   the-mandalore-project/about.rst
   the-mandalore-project/python-wrapper.rst
   the-mandalore-project/docker-images.rst
   the-mandalore-project/offline-resources.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Mandalore wrapper

   mandalore-wrapper/install.rst
   mandalore-wrapper/start.rst
   mandalore-wrapper/info.rst
   mandalore-wrapper/exec.rst
   mandalore-wrapper/update.rst
   mandalore-wrapper/upgrade.rst
   mandalore-wrapper/stop.rst
   mandalore-wrapper/restart.rst
   mandalore-wrapper/remove.rst
   mandalore-wrapper/uninstall.rst
   mandalore-wrapper/version.rst
   mandalore-wrapper/advanced-uses.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Mandalore image

   mandalore-image/tools.rst
   mandalore-image/my-resources.rst
   mandalore-image/credentials.rst
   mandalore-image/services.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Mandalore resources

   mandalore-resources/resources.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Community

   community/users.rst
   community/contributors.rst
   community/maintainers.rst
