import click
import re
from script import commands
from script import custom_types
from script import lib


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
        click.echo(out)
    except Exception:
        click.echo("BAD PATTERN")
        exit(-1)


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
@click.option(
    '--ignore',
    '-i',
    help='Ignore all directories inside --dir-name equals to some --ignore',
    type=custom_types.List()
)
def dir(replace, by, extension, dir_name, yes, ignore):
    for path, dirs, files in lib.walk(dir_name, ignore or [], extension):
        for f in files:
            file_name = '{}/{}'.format(path, f)
            commands.file(replace, by, file_name, yes)

            
if __name__ == '__main__':
    main()
