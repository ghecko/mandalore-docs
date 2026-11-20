===========
Maintainers
===========

This part of the documentation is meant for Mandalore maintainers. It adds up to the :doc:`contributors </community/contributors>` documentation.

.. contents::
    :local:

Wrapper release
===============

.. hint::
    The wrapper documentation must be aligned with the wrapper features. The docs PR can be merged once the wrapper is released.

Preparation
-----------

#. Update the wrapper repository and its submodules (``mandalore-images`` and ``mandalore-resources``) to the commits that must be shipped with the release, and commit the submodule updates.

   .. code-block:: bash

       git pull
       git submodule update --init --remote
       git add mandalore-images mandalore-resources

#. Run the checks (the same as the CI):

   .. code-block:: bash

       mypy ./mandalore/ --ignore-missing-imports --check-untyped-defs
       mypy ./mandalore.py --ignore-missing-imports --check-untyped-defs
       python3 -m pytest

#. Review the release configuration:

   * ``mandalore/config/ConstantConfig.py``: version number (``__version__``, without alpha or beta tag for a release).
   * ``mandalore/utils/imgsync/spawn.sh``: must contain a line with the script current version in the following format: ``# Spawn Version:2``.
   * ``tests/mandalore_test.py``, ``README.md`` and this documentation.

#. Check that the package builds and contains the image scripts:

   .. code-block:: bash

       uv build   # or: python3 -m build
       unzip -l dist/*.whl | grep -E "spawn.sh|entrypoint.sh"

Publish
-------

Once the pull request is merged on the default branch, push a version tag (``X.Y.Z``) to run the `release workflow <https://github.com/ghecko/mandalore/actions/workflows/entrypoint_release.yml>`_:

.. code-block:: bash

    git tag -s 4.4.0 -m '4.4.0'
    git push origin 4.4.0

The release workflow runs the tests and builds the Python distributions. Publishing to PyPI is **disabled** until the PyPI project and its trusted publisher are configured: set the repository variable ``PYPI_PUBLISH`` to ``true`` to enable it.

Finally, create the GitHub **release** for the new tag.

Images release
==============

Images are built locally and pushed to the GitHub Container Registry (``ghcr.io/ghecko/mandalore``).

Build
-----

The builds use the ``Makefile`` of the `mandalore-images <https://github.com/ghecko/mandalore-images>`_ repository. The image version is set with ``VERSION`` (stored in the ``org.mandalore.version`` label). A GitHub token (no scope needed) avoids the GitHub API rate-limit during the build; it is passed as a BuildKit secret and never stored in the image (see the images README).

.. code-block:: bash

    export GITHUB_TOKEN=ghp_...
    make base VERSION=2.0.0
    make full VERSION=2.0.0

.. warning::
    Building the ``full`` image requires a lot of disk space (around 50GB for the final image, more during the build): standard GitHub-hosted runners are not enough.

Publish
-------

Each published image needs two tags: ``<image>`` (e.g. ``full``), which users install, and ``<image>-<version>`` (e.g. ``full-2.0.0``), used by the wrapper to display the image version and detect updates.

Pushing requires a **classic** GitHub token with the ``write:packages`` scope (fine-grained tokens are not supported by GHCR).

.. code-block:: bash

    echo "$TOKEN" | docker login ghcr.io -u <github_user> --password-stdin
    docker tag <built image> ghcr.io/ghecko/mandalore:full
    docker tag ghcr.io/ghecko/mandalore:full ghcr.io/ghecko/mandalore:full-2.0.0
    docker push ghcr.io/ghecko/mandalore:full
    docker push ghcr.io/ghecko/mandalore:full-2.0.0

A new GHCR package is **private** by default: either make it public in the package settings on GitHub, or users must run ``docker login ghcr.io`` (token with ``read:packages``) before installing images.

Before publishing an image, make sure no secret ended up in it (``docker history --no-trunc`` and ``docker inspect`` must not show any token).

Finally, create a git tag and a GitHub release on the mandalore-images repository for the new version.

Documentation
=============

The documentation is built with Sphinx:

.. code-block:: bash

    python3 -m pip install -r requirements.txt
    sphinx-build -b html source build/html

The ``source/assets/exegol_resources/resources_list.csv`` file is updated automatically by the mandalore-resources workflow (do not rename this folder without updating that workflow).

Pull Requests
=============

When handling pull requests, maintainers may need to `synchronize a contributor's fork with latests changes <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>`_. In command-line, this can be achieved as follows.

.. code-block:: bash

    git clone "git@github.com:USER/FORK" "dest_dir"
    cd dest_dir
    git remote add upstream "git@github.com:ghecko/REPO"
    git fetch upstream
    git checkout "TARGET_FORK_BRANCH"
    git merge --no-edit upstream/"ORIGIN_BRANCH"
    # solve conflicts if any
    git push
