from jinja2 import Environment, PackageLoader


TEMPLATES_DIR = 'templates'
TEMPLATE_ENV = Environment(loader=PackageLoader(__name__, TEMPLATES_DIR))
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight)']
DOCUMENT_TEMPLATE='document.html'