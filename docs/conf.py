import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import dlestxetx  # NoQA

project = 'dlestxetx Python Module'
version = release = dlestxetx.__version__
# noinspection PyShadowingBuiltins
copyright = '2019, Alex Peters'
author = 'Alex Peters'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_last_updated_fmt = '%d %B %Y'
html_show_sphinx = False
html_theme_options = {
    'style_external_links': True,
}
