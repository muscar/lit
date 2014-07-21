import os

from contextlib import contextmanager
from jinja2 import Environment, PackageLoader


PACKAGE_PATH=os.path.split(__file__)[0]
TEMPLATES_DIR = 'templates'
CSS_DIR = 'css'
CSS_PATH = os.path.join(PACKAGE_PATH, CSS_DIR)
TEMPLATE_ENV = Environment(loader=PackageLoader('lit', TEMPLATES_DIR))
DOCUMENT_TEMPLATE='document.html'
CSS_DEFAULT_STYLE_FILE='git.css'
CSS_CLASS_NAME='highlight'
KNOWN_FORMATS = set(['html', 'code'])



def css_file_contents(path):
    with open(os.path.join(CSS_PATH, path), 'r') as f:
        return f.read()
