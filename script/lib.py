import io
import re
import os


def replace_file(replace, by, file_name):
    with io.open(file_name, 'r') as f:
        lines = f.readlines()

    return replace_lines(replace, by, lines)


def replace_lines(replace, by, lines):
    new, diff = [], []
    for line in lines:
        new.append(replace_line(replace, by, line))
        if new[-1] != line:
            diff.append((line, new[-1]))
    return lines, new, diff


def replace_line(replace, by, line):
    new = re.sub(replace, by, line)
    return new


def walk(dir_name: str, ignore: list, extension: str = None) -> iter:
    for path, dirs, files in os.walk(dir_name, topdown=True):
        dirs[:] = [d for d in dirs if d not in ignore]
        if extension:
            files[:] = [
                f for f in files if f.endswith('.{}'.format(extension.lstrip('.')))
            ]
        yield (path, dirs, files)