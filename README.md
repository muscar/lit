# Python literate programming

This is a simple literate programming tool written in Python. It uses [Github
Flavoured Markdown](https://help.github.com/articles/github-flavored-markdown
"Github Flavoured Markdown").

## Usage

Just write your document in Markdown and run this tool giving it an output
format as ab argument and the path to the source of your file, e.g.

    ./lit.py -f html samples/hello.md > samples/hello.html

to generate HTML output. The supported formats are `md` for Markdown, `html`
for HTML and `code` to extract the code blocks from the document.

## Dependencies

The tool uses [Jinja2](http://jinja.pocoo.org/docs/ "Jinja2") for templating
and [Markdown module](http://pythonhosted.org//Markdown/ "Markdown module")
for Python with [Pygments](http://pygments.org/ "Pygments") for syntax
highlighting.