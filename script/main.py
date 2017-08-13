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
@click.option('--yes', '-y', is_flag=True, help='If is true, replace all')
@click.option('--ignore', '-i', help='Ignore all directories inside --dir-name equals to some --ignore')
def dir(replace, by, extension, dir_name, yes, ignore):
    for path, dirs, files in os.walk(dir_name):
        path_as_list = path.split('/')
        ignore_as_list = ignore.split(',')
        if any(filter(lambda x: x in ignore_as_list, path_as_list)):
            continue
        for f in files:
            ext = f.split('.')
            if len(ext) > 1:
                ext = ext[-1]
            file_name = '{}/{}'.format(path, f)
            if not extension or ext == extension:
                commands.file(replace, by, file_name, yes)

            
if __name__ == '__main__':
    main()