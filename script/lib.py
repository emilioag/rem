import io
import re


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