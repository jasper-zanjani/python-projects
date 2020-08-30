import click

class Starship:
    def __init__(self, name, registry, crew):
        self.name = name
        self.registry = registry
        self.crew = crew
        self.battlestations = False
    def redalert(self):
        self.battlestations = True
    def standdown(self):
        self.battlestations = False
    def __str__(self):
        return f'USS {self.name} {self.registry}, {self.crew} strong'

# main = click.CommandCollection(sources=[ g1 ])

@click.group()
def main():
    pass

@main.group()
def ship():
    pass

@ship.command('build')
@click.option('--name',default='Enterprise')
@click.option('--registry',default='NCC-1701')
@click.option('--crew',default=600)
def commission(name, registry, crew):
    print(Starship(name, registry, crew))

if __name__ == '__main__':
    main()

