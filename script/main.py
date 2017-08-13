import click
import re
import os
from script import commands


@click.group()
def main():
    pass


@main.command()
@click.option('--replace', '-r')
@click.option('--by', '-b')
@click.option('--text', '-t')
def stdin(replace, by, text):
    try:
        out = re.sub(replace, by, text)
    except Exception:
        click.echo("BAD PATTERN")
        exit(-1)
    click.echo(out)

@main.command()
@click.option('--replace', '-r')
@click.option('--by', '-b')
@click.option('--file-name', '-f')
@click.option('--yes', '-y', is_flag=True)
def file(replace, by, file_name, yes):
    commands.file(replace, by, file_name, yes)
        

@main.command()
@click.option('--extension', '-e')
@click.option('--replace', '-r')
@click.option('--by', '-b')
@click.option('--dir-name', '-d')
@click.option('--yes', '-y', is_flag=True)
@click.option('--ignore', '-i')
def dir(replace, by, extension, dir_name, yes, ignore):
    for path, dirs, files in os.walk(dir_name):
        path_as_list = path.split('/')
        if path_as_list and ignore and path.split('/')[-1] in ignore.split(','):
            continue
        for f in files:
            file_name = '{}/{}'.format(path, f)
            commands.file(replace, by, file_name, yes)
            
if __name__ == '__main__':
    main()