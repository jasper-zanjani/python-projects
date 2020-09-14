# Grouping all command groups into an entry-point group will allow nexted command groups, similar to the syntax
# used in complex utility suites like netsh and git

import click

@click.group()
def cli()
    pass

@cli.group()
def warmup():
    pass

@cli.group()
def workout():
    pass

@warmup.command('stretch')
@click.argument('time')
def warmup_stretch(time):
    print(f'Stretching for {time} minutes...')

@warmup.command('warmup')
@click.argument('time')
def warmup_warmup(time):
    print(f'Warming up for {time} minutes...')

@workout.command('chest')
@click.argument('weight')
def workout_chest(weight):
    print(f'Working out chest with {weight} lbs. of weight!')

@workout.command('legs')
@click.argument('weight')
def workout_chest(weight):
    print(f'Working out legs with {weight} lbs. of weight!')

if __name__ == '__main__':
    cli()
