#!/usr/bin/env python3

import argparse
import itertools as it
import sys

from lit.lib import fragment
from lit.lib.document import Document


def read_fragment(input_file):
    with fragment.from_line(input_file.readline()) as frag:
        for line in it.takewhile(lambda line: not frag.isendmarker(line), input_file):
            frag.append(line)
        return frag


def read(input_file):
    doc = Document()
    fragment = read_fragment(input_file)
    while len(fragment) > 0:
        doc.append(fragment)
        fragment = read_fragment(input_file)
    return doc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--format', help='the output format', choices=['html', 'code'])
    parser.add_argument('file', help='the markdown source file')

    args = parser.parse_args()

    with open(args.file, 'r') as input_file:
        doc = read(input_file)
        print(getattr(doc, args.format)())


if __name__ == '__main__':
    main()
