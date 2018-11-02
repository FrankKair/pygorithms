#!/usr/bin/env python3
import os
from subprocess import check_output


def format_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    print('Formatting:')
    for filename in os.listdir(dir_path):
        if filename.endswith(".py") and len(filename) == 6:
            print(filename)
            command = f"yapf -i {filename}"
            check_output(command, shell=True)


if __name__ == '__main__':
    format_files()
