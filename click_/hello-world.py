import click


@click.command()
@click.option('--arg', '-a',
              default='world',
              help='Specify who to say hello to!',
              prompt="What is your name? ")
def hello(arg):
    print(f'Hello {arg}!')


if __name__ == '__main__':
    hello()
