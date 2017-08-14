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


class List(click.ParamType):
    name = 'list'

    def convert(self, value, param, ctx):
        try:
            if not isinstance(value, str):
                raise ValueError
            else:
                return value.split(',')
        except ValueError:
            self.fail('%s is not a valid yes/no' % value, param, ctx)