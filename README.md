# Python literate programming

This is a simple literate programming tool written in Python. It uses [Github
Flavoured Markdown](https://help.github.com/articles/github-flavored-markdown
"Github Flavoured Markdown").

## Usage

Just write your document in Markdown and run this tool giving it an output
format as ab argument and the path to the source of your file, e.g.

    lit -f html samples/hello.md > samples/hello.html

to generate HTML output. The supported formats are `html` for HTML and `code`
to extract the code blocks from the document.

You can also specify the CSS class for highlighted blocks via the `-c` switch:

    lit -f html -c listing samples/hello.md > samples/hello.html

The `-s` flag allows you to choose of whether lit generates the CSS style
inline in the head of the HTML document or if it uses an external file.

    lit -f html -s inline samples/hello.md > samples/hello.html

will generate the CSS definitions inline, while

    lit -f html -s mystyle.css samples/hello.md > samples/hello.html

will use the `mystyle.css` file.

## Installation

    $ git clone https://github.com/muscar/lit.git
    $ cd lit
    $ python setup.py sdist
    $ pip install dist/lit-0.1.tar.gz

## Dependencies

The tool uses [Jinja2](http://jinja.pocoo.org/docs/ "Jinja2") for templating
and [Markdown module](http://pythonhosted.org//Markdown/ "Markdown module")
for Python with [Pygments](http://pygments.org/ "Pygments") for syntax
highlighting.
