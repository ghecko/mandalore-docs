Docker images
=============

The Docker images are the heart of the Mandalore project. A neat choice of tools, configurations, aliases, history commands, and various customizations are prepared in multiple images adapted for multiple uses: web hacking, Active Directory, OSINT (Open Source INTelligence), etc.

All images are available on `the GitHub Container Registry <https://github.com/ghecko/mandalore/pkgs/container/mandalore>`_. This allows to offer pre-built, compressed images, so that users don't have to build their own image, but users that choose to do so can. Pulling pre-built images, or building one, can be done with ``mandalore install`` (documentation
:doc:`here </mandalore-wrapper/install>`).

============= =====================================================================================================
  Image name   Description
============= =====================================================================================================
  full         Includes all the tools supported by Mandalore (warning: this is the heaviest image)
  ad           Includes tools for Active Directory / internal pentesting only.
  web          Includes tools for Web pentesting only.
  light        Includes the lightest and most used tools for various purposes.
  osint        Includes tools for OSINT.
============= =====================================================================================================

Images are published as ``ghcr.io/ghecko/mandalore:<image name>``, with an additional versioned tag (e.g. ``full-2.0.0``) used by the wrapper to display the image version. Not every image is necessarily published at a given time: run ``mandalore info`` to see the images actually available. Any image can also be built locally from the `mandalore-images <https://github.com/ghecko/mandalore-images>`_ repository (``mandalore install <name> <profile>``).

.. hint::

   While the registry package is private, run ``docker login ghcr.io`` (GitHub token with the ``read:packages`` scope) before using ``mandalore install`` or ``mandalore update``.

.. note::

   Mandalore uses Docker images and containers. Understanding the difference is essential to understand Mandalore.

   * **image**: think of it as an immutable template. They cannot be executed as-is and serve as input for containers. It's not possible to open a shell in an image.
   * **container**: a container rests upon an image. A container is created for a certain image at a certain time. It's possible to open a shell in a container. Careful though, once a container is created, updating the image it was created upon won't have any impact on the container. In order to enjoy the new things, a new container must be created upon that updated image, which is what :doc:`mandalore upgrade </mandalore-wrapper/upgrade>` does while keeping the container configuration and data.
