import os
import sys
sys.path.insert(0, os.path.abspath('.'))


project = 'Syntetic index price calculation'
copyright = '2021, Aitor Díaz Medina'
author = 'Aitor Díaz Medina'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
]
autodoc_typehints = "description"
html_theme = "furo"
