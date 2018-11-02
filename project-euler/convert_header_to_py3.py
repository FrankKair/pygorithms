#!/usr/bin/env python3
import os


def convert_header_to_python3():
    directory = os.path.dirname(__file__)

    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename.startswith("0"):
            lines = []
            with open(os.path.join(directory, filename), 'r+') as file:
                lines = file.readlines()[1:]
                file.truncate()

            with open(os.path.join(directory, filename), 'r+') as file:
                file.writelines(['#!/usr/bin/env python3', '\n'] + lines)

        else:
            continue


if __name__ == '__main__':
    convert_header_to_python3()
