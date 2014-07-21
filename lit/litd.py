import argparse
import os
import sys
import subprocess
import termcolor
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


FORMAT_EXTENSIONS = {'html':'.html',
                     'code':'.py'}


class EventHandler(FileSystemEventHandler):
    def __init__(self, formats):
        super().__init__()
        self.formats = formats

    def on_modified(self, event):
        fullname, ext = os.path.splitext(event.src_path)
        if not event.is_directory and event.event_type == 'modified' and ext == '.md':
            print('{0} was modified; running lit'.format(event.src_path))
            for format in self.formats:
                ext = FORMAT_EXTENSIONS[format]
                output_name = fullname + ext
                with open(output_name, 'w+') as output:
                    try:
                        output.write(subprocess.check_output(['lit', '-f', format, event.src_path]).decode('utf-8'))
                        print('wrote {0}'.format(output_name))
                    except subprocess.CalledProcessError as ex:
                        print(termcolor.colored('the lit process exited with a non-zero return code ({0})'.format(ex.returncode), 'red'))
                        print(termcolor.colored('command output:', 'red'))
                        print(ex.output.decode('utf-8'))


def watch(path, formats):
    event_handler = EventHandler(formats)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--formats', help='the output format(s)', default='html')

    args = parser.parse_args()
    formats = []
    for format in args.formats.split(','):
        if format in FORMAT_EXTENSIONS:
            formats.append(format)
        else:
            print(termcolor.colored('ignoring unknown format {0}'.format(format), 'yellow'))

    watch('.', formats)


if __name__ == "__main__":
    main()
