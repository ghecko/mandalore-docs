========================
:code:`uninstall` action
========================

The purpose of the ``uninstall`` action is to remove one or more Mandalore images.

.. warning::
    The wrapper will try to delete the selected mandalore images but this can only work if the selected images are **not used by any container** anymore. A container based on an image that doesn't exist anymore cannot run.

Options
=======

The options of the ``uninstall`` action are limited to selecting the image(s) to be removed, and forcing the removal without asking the user for interactive confirmation.

========================= =============
 Option                    Description
========================= =============
``IMAGE``                 Tag used to target one or more Mandalore images
``--all``                 Select every installed Mandalore image
``-F``, ``--force``       Remove image without interactive user confirmation.
========================= =============


Command examples
================

.. code-block:: bash

    # Uninstall interactively one or more images:
    mandalore uninstall

    # Uninstall the "full" image:
    mandalore uninstall "full"

    # Uninstall the "full", "ad" and "web" images without asking for user confirmation:
    mandalore uninstall -F "full" "ad" "web"

    # Uninstall every installed image:
    mandalore uninstall --all
