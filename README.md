# Python literate programming

This is a simple literate programming tool written in Python. It uses [Github
Flavoured Markdown](https://help.github.com/articles/github-flavored-markdown
"Github Flavoured Markdown").

## Usage

Just write your document in Markdown, give it an extension starting with
"lit", e.g. ".litpy", and run `lit` giving it an output format as an
argument and the path to the source of your file, e.g. invoke `lit` like this:

    $ lit -f html samples/hello.litpy
    wrote samples/hello.html

to generate HTML output. The supported formats are `html` for HTML and `code`
to extract the code blocks from the document.

You can also specify the CSS class for highlighted blocks via the `-c` switch:

    $ lit -f html -c listing samples/hello.md
    wrote samples/hello.html

The `-s` flag allows you to choose of whether lit generates the CSS style
inline in the head of the HTML document or if it uses an external file.

    $ lit -f html -s inline samples/hello.md
    wrote samples/hello.html

will generate the CSS definitions inline, while

    $ lit -f html -s mystyle.css samples/hello.md
    wrote samples/hello.html

will use the `mystyle.css` file.

Passing a directory path instead of a file path to `lit` will start the tool in
"watch mode", i.e. `lit` watches the directory for any changes to literate
source file and automatically generates the output formats selected with `-f`:

    $ lit -f html,code samples/
    watching samples/

Note that you can also specify multiple formats by separating them with a
comma.

Invoke `lit` with the `-h` option to get help:

    usage: lit [-h] [-f FORMATS] [-c CSS_CLASS_NAME] [-s STYLESHEET] file

    positional arguments:
      file                  the literate source file (.lit*, e.g. .litpy) or a
                            directory to watch

    optional arguments:
      -h, --help            show this help message and exit
      -f FORMATS, --formats FORMATS
                            the output format(s)
      -c CSS_CLASS_NAME, --css-class-name CSS_CLASS_NAME
                            the CSS class name for highlighted blocks
      -s STYLESHEET, --stylesheet STYLESHEET
                            either generate CSS inline (pass "inline") or the path
                            to the CSS file to include

## Installation

    $ git clone https://github.com/muscar/lit.git
    $ cd lit
    $ python setup.py sdist
    $ pip install dist/lit-0.1.tar.gz

## Dependencies

The tool uses [Jinja2](http://jinja.pocoo.org/docs/ "Jinja2") for templating
and [Markdown module](http://pythonhosted.org//Markdown/ "Markdown module")
for Python with [Pygments](http://pygments.org/ "Pygments") for syntax
highlighting. It also uses
[watchdog](https://github.com/gorakhargosh/watchdog "watchdog") while for
"watch mode".
