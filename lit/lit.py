#!/usr/bin/env python3

import argparse
import itertools as it
import os
import sys
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from lit import config
from lit.lib import fragment
from lit.lib.document import Document


def is_literate_ext(ext):
    return ext.startswith('.lit')


def code_file_ext(literate_ext):
    return literate_ext.replace('lit', '')


def output_file_name(path, format):
    fullname, ext = os.path.splitext(path)
    assert(is_literate_ext(ext))
    if format == 'html':
        return fullname + '.html'
    return fullname + code_file_ext(ext)


def read_fragment(input_file):
    with fragment.from_line(input_file.readline()) as frag:
        for line in it.takewhile(lambda line: not frag.isendmarker(line), input_file):
            frag.append(line)
        return frag


def read(path, css_class_name, stylesheet):
    with open(path, 'r') as input_file:
        doc = Document(css_class_name, stylesheet)
        fragment = read_fragment(input_file)
        while len(fragment) > 0:
            doc.append(fragment)
            fragment = read_fragment(input_file)
        return doc


def process_file(path, args):
    formats = config.KNOWN_FORMATS & set(args.formats.split(','))
    doc = read(path, args.css_class_name, args.stylesheet)
    for format in formats:
        output_path = output_file_name(path, format)
        with open(output_path, 'w+') as output_file:
            output_file.write(getattr(doc, format)())
        print('wrote {0}'.format(output_path))


class EventHandler(FileSystemEventHandler):
    def __init__(self, args):
        super().__init__()
        self.args = args

    def on_modified(self, event):
        _, ext = os.path.splitext(event.src_path)
        if not event.is_directory and event.event_type == 'modified' and is_literate_ext(ext):
            print('{0} was modified; running lit'.format(event.src_path))
            process_file(event.src_path, self.args)


def watch(path, args):
    event_handler = EventHandler(args)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print('watching {0}'.format(path))
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--formats', help='the output format(s)', default='html')
    parser.add_argument('-c', '--css-class-name', help='the CSS class name for highlighted blocks', default=config.CSS_CLASS_NAME)
    parser.add_argument('-s', '--stylesheet', help='either generate CSS inline (pass "inline") or the path to the CSS file to include', default='inline')
    parser.add_argument('file', help='the literate source file (.lit*, e.g. .litpy) or a directory to watch')

    args = parser.parse_args()
    formats = config.KNOWN_FORMATS & set(args.formats.split(','))

    if os.path.isdir(args.file):
        watch(args.file, args)
    else:
        process_file(args.file, args)


if __name__ == '__main__':
    main()
