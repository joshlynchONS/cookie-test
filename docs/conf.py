"""Sphinx configuration."""
project = "Cookie Test"
author = "Joshua Lynch"
copyright = "2023, Joshua Lynch"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
