#!/usr/bin/env python3

import argparse
import sys

from lib.fragment import FragmentMeta
from lib.document import Document


def read(input_file):
    doc = Document()
    fragment = FragmentMeta.make(input_file.readline())

    for line in input_file:
        if fragment.isendmarker(line):
            doc.append(fragment.finalize())
            fragment = FragmentMeta.make(input_file.readline())
        else:
            fragment.append(line)
    else:
        doc.append(fragment.finalize())
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
