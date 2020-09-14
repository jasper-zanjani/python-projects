import jenkins
import click
import dotenv
import os

@click.group()
def api():
    pass

@api.command()
def jobs(_list):
    pass

if __name__ == '__main__':
    api()

