import datetime
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mandalore'
copyright = f'{datetime.datetime.now().year}, Mandalore contributors (fork of Exegol by Shutdown & Dramelac)'
author = 'Mandalore contributors'
# release = '4.1.0'  # Disable version for doc

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinx_tabs.tabs',
              'sphinx_copybutton',
              "sphinxcontrib.jquery"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# Published with GitHub Pages
html_baseurl = 'https://ghecko.github.io/mandalore-docs/'
# "Edit on GitHub" links
html_context = {
    'display_github': True,
    'github_user': 'ghecko',
    'github_repo': 'mandalore-docs',
    'github_version': 'main',
    'conf_py_path': '/source/',
}
html_static_path = ['_static']


# Tabs options
sphinx_tabs_disable_tab_closing = True

def setup(app):
  app.add_css_file("css/custom.css")
