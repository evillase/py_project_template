# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys
from datetime import datetime

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath(".."))

# TODO maybe move this function to project_dir/project_meta.py
# if more places need this and if __init__.py needs this to update version?
def _get_project_meta():
    import os

    import toml

    cfg_toml = os.path.join(os.path.abspath(".."), "pyproject.toml")
    with open(cfg_toml, "r") as f:
        pyproject = toml.load(f)
    return pyproject["tool"]["poetry"]


# -- Project information -----------------------------------------------------

meta_data = _get_project_meta()
project = str(meta_data["name"])
author = str(meta_data["authors"][0])
year = datetime.now().year
copyright = f"{year}, Intel"

# short version
version = str(meta_data["version"])
# full version including alpha/beta tags
release = version

rst_prolog = f"""
.. |project| replace:: {project}
.. |version| replace:: {version}
.. |author| replace:: {author}
"""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "releases",
]

pygments_style = "sphinx"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

todo_include_todos = True
# releases_github_path = 'intel-sandbox/<project-name>'
releases_unstable_prehistory = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# html_logo = f"{html_static_path[0]}/imgs/logo.png"
