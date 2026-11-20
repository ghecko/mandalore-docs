===============
About Mandalore
===============

Origin
======

Mandalore is a fork of `Exegol <https://github.com/ThePorgs/Exegol>`_, the community-driven hacking environment created by `ThePorgs <https://github.com/ThePorgs>`_.

The fork was started from **Exegol 4.3.12**, the GPLv3 code base, before Exegol 5 moved to a different licence. Mandalore keeps the GPLv3 licence and will always remain free, continuing the original philosophy with a focus on usability, extensibility, and community contribution.

All credits for the original design, code and documentation go to the Exegol authors and contributors. This documentation itself is derived from the Exegol documentation (GPLv3).

What is different from Exegol
=============================

* **Names**: the command is ``mandalore``, the configuration lives in ``~/.mandalore``, image labels use the ``org.mandalore.*`` prefix and in-container files are under ``/.mandalore``.
* **Images** are published on the GitHub Container Registry as ``ghcr.io/ghecko/mandalore:<tag>`` (no Docker Hub). While the package is private, run ``docker login ghcr.io`` first, the wrapper reuses your Docker credentials. Local images built under the former image name are automatically retagged with the new name.
* **Repositories** are hosted on GitHub: `mandalore <https://github.com/ghecko/mandalore>`_ (wrapper), `mandalore-images <https://github.com/ghecko/mandalore-images>`_, `mandalore-resources <https://github.com/ghecko/mandalore-resources>`_ and `mandalore-docs <https://github.com/ghecko/mandalore-docs>`_.
* **Python 3.10+** is required by the wrapper.
* **Added features**: the :doc:`upgrade </mandalore-wrapper/upgrade>` action (move a container to a newer image while keeping its configuration and data), the ``--all`` selector on ``stop``, ``remove``, ``uninstall`` and ``upgrade``, and container / workspace disk usage in :doc:`info </mandalore-wrapper/info>`.
* **Not available**: Exegol 5 features (Exegol Pro/Enterprise licensing, account, etc.) are not part of Mandalore.

Licence
=======

The wrapper, images, resources and this documentation are distributed under the `GNU GPLv3 <https://www.gnu.org/licenses/gpl-3.0.html>`_ licence. Third-party tools shipped in the images and resources keep their own licences.
