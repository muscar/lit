import re

from markdown import markdown

from lib.fragment import CodeFragment

import config


class Document(object):
    def __init__(self):
        self.fragments = []

    def append(self, fragment):
        self.fragments.append(fragment)

    def _md(self):
        return '\n'.join([repr(fragment) for fragment in self.fragments])

    def html(self):
        template = config.TEMPLATE_ENV.get_template(config.DOCUMENT_TEMPLATE)
        body = markdown(self._md(), extensions=config.MARKDOWN_EXTENSIONS)
        return template.render(body=body)

    def code(self):
        return '\n\n'.join(str(fragment) for fragment in self.fragments if isinstance(fragment, CodeFragment))
