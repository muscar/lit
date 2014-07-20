from jinja2 import Environment, PackageLoader


TEMPLATES_DIR = 'templates'
TEMPLATE_ENV = Environment(loader=PackageLoader('lit', TEMPLATES_DIR))
DOCUMENT_TEMPLATE='document.html'
CSS_CLASS_NAME='highlight'