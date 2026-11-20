Updates
=======

The whole Mandalore can be updated through its own wrapper with ``mandalore update`` (documentation
:doc:`here </mandalore-wrapper/update>`).

.. hint::

   Wrappers installed as a package (uv, pipx or pip, not editable) don't support auto-update. The wrapper itself can then be updated as follows.

   .. code-block:: bash

      uv tool upgrade mandalore
      # OR
      pipx upgrade mandalore

Updating an image does not modify existing containers. Once an image is updated, existing containers can be moved to it with ``mandalore upgrade`` (documentation
:doc:`here </mandalore-wrapper/upgrade>`).
