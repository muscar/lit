import re

from markdown import markdown

from lit import config
from lit.lib.fragment import CodeFragment


class Document(object):
    def __init__(self, css_class_name, stylesheet):
        self.stylesheet = stylesheet
        self.markdown_exts = ['fenced_code', 'codehilite(css_class={0})'.format(css_class_name)]
        self.fragments = []

    def append(self, fragment):
        self.fragments.append(fragment)

    def _md(self):
        return '\n'.join(repr(fragment) for fragment in self.fragments)

    def html(self):
        template = config.TEMPLATE_ENV.get_template(config.DOCUMENT_TEMPLATE)
        body = markdown(self._md(), extensions=self.markdown_exts)
        css = None
        if self.stylesheet == 'inline':
            css = config.css_file_contents(config.CSS_DEFAULT_STYLE_FILE)
        return template.render(body=body, stylesheet=self.stylesheet, css=css)

    def code(self):
        code_fragments = (str(fragment).rstrip() for fragment in self.fragments
                          if isinstance(fragment, CodeFragment))
        return '\n'.join(code_fragments)
