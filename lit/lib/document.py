import re

from markdown import markdown

from lit import config
from lit.lib.fragment import CodeFragment


class Document(object):
    def __init__(self, css_class_name):
        self.fragments = []
        self.markdown_exts = ['fenced_code', 'codehilite(css_class={0})'.format(css_class_name)]

    def append(self, fragment):
        self.fragments.append(fragment)

    def _md(self):
        return '\n'.join([repr(fragment) for fragment in self.fragments])

    def html(self):
        template = config.TEMPLATE_ENV.get_template(config.DOCUMENT_TEMPLATE)
        body = markdown(self._md(), extensions=self.markdown_exts)
        return template.render(body=body)

    def code(self):
        return '\n\n'.join(str(fragment) for fragment in self.fragments if isinstance(fragment, CodeFragment))
