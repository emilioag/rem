import io
import click
from script.custom_types import YesNo
from script.lib import replace_file


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
            try:
                with io.open(file_name, 'w') as f:
                    f.writelines(new)
                click.secho("REPLACED: {}".format(file_name), fg='green')
            except Exception as e:
                click.secho(e, bg='red')
        else:
            click.secho("PASS: {}".format(file_name), fg='green')
    else:
        click.secho("NO MATCHES FOUND: {}".format(file_name), fg='red')