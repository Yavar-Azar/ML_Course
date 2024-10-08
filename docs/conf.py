# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Machine-Learning'
copyright = '2024, Yavar'
author = 'Yavar'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'nbsphinx',  # Add this line
    'sphinx.ext.mathjax',  # Assuming you have this and possibly other extensions
    'sphinx_book_theme',]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

nbsphinx_execute = 'always'
nbsphinx_allow_errors = False  # Set to True if you want to include notebooks even if they have errors
nbsphinx_prompt_width = '0'  # Disable prompts before input
html_scaled_image_link = False  # Avoid scaling of images
nbsphinx_output_format = 'svg'  # Use 'svg' for vector graphics or 'png' for raster graphics

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
