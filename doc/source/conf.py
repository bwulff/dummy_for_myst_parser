# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dummy'
copyright = '2022, Ben'
author = 'Ben'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	"autoapi.extension",
	"sphinx_rtd_theme",
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []

autoapi_type = 'python'
autoapi_dirs = ['../../src']

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "linkify",                  # trun URLs into links automatically
    "dollarmath",               # support for $..$ and $$..$$ math environments
    "substitution",             # enable jina2 style substitutions
    "deflist",                  # enable markup for Pandoc style definitions 
    "html_image",               # enable support for HTML image tags
    "html_admonition",          # enable support for HTML info/warning/tip boxes
    "colon_fence",              # enable support for colon fence environment, e.g. for figure-md
]
myst_dmath_double_inline = True   # enable support for inline $$-blocks 
myst_heading_anchors = 4          # enable automatic anchor generation down to n-th level headings

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
