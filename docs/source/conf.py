
import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

project = "API Gateway"
copyright = "2020, IIJGSI"
author = "IIJGSI"
version = '0.0.1'
release = '0.0.1'
templates_path = ["_templates"]
extensions = ["sphinx.ext.autodoc", "sphinx.ext.doctest"]
source_suffix = ".rst"
master_doc = "index"
pygments_style = "sphinx"
html_theme = "alabaster"
html_logo = "_static/logo.png"
html_static_path = ["_static"]
pygments_style = "sphinx"