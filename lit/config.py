from jinja2 import Environment, PackageLoader


TEMPLATES_DIR = 'templates'
TEMPLATE_ENV = Environment(loader=PackageLoader('lit', TEMPLATES_DIR))
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite(css_class=highlight)']
DOCUMENT_TEMPLATE='document.html'