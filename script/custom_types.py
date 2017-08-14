import click


class YesNo(click.ParamType):
    name = 'bool'

    def convert(self, value, param, ctx):
        try:
            if value.lower() in ['yes', 'y']:
                return True
            elif value.lower() in ['no', 'n']:
                return False
            else:
                raise ValueError
        except ValueError:
            self.fail('%s is not a valid yes/no' % value, param, ctx)