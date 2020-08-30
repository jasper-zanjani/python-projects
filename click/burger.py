import click
from enum import Enum

@click.group()
def cli():
    pass

@cli.group()
def lunch():
    pass

@cli.group()
def dinner():
    pass

class Doneness(Enum):
    WELLDONE="well-done"
    MEDIUM='medium'
    RARE='rare'

@click.command()
@click.option('--doneness',type=click.Choice(['well-done','medium','rare']),required=True)
def burger(doneness):
    print(f'Have a {doneness} burger!')

lunch.add_command(burger)
dinner.add_command(burger)


if __name__ == '__main__':
    cli()
