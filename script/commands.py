import click
from types import YesNo
from lib import replace_file


def file(replace, by, file_name, yes):
    lines, new, diff = replace_file(replace, by, file_name)
    if diff:
        click.secho("FOUND: {}".format(file_name), fg='white', bg='blue')
        for i, j in diff:
            click.secho("- {}".format(i), fg='green')
            click.secho("+ {}".format(j), fg='red')
        if not yes:
            yes = click.prompt('Do you want to replace it? [y/N]', type=YesNo(), default=False)
        if yes:
            click.secho("REPLACED: {}".format(file_name), fg='green')
        else:
            click.secho("PASS: {}".format(file_name), fg='green')
    else:
        click.secho("NO MATCHES FOUND: {}".format(file_name), fg='red')