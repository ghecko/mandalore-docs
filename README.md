> **📌 This repository hosts the Mandalore documentation, a sub-repository of the Mandalore project.
> If you were looking for Mandalore, go to [the main repo](https://github.com/ghecko/mandalore)**
___

# Mandalore docs

This repository hosts the source of the documentation for users, contributors, developers (work in progress), and maintainers (work in progress).

Mandalore is a fork of [Exegol](https://github.com/ThePorgs/Exegol) 4.3.12 (GPLv3). This documentation is derived from the [Exegol documentation](https://github.com/ThePorgs/Exegol-docs), under the same GPLv3 licence.

## Build

```bash
python3 -m pip install -r requirements.txt
sphinx-build -b html source build/html
```

The pages are in `source/` (reStructuredText, Sphinx). Open a pull request against the default branch.
