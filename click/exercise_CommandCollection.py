# CommandCollection will flatten out all grouped commands, presenting them as the first tier of commands
# to the end-user.

import click

@click.group()
def warmup():
    pass

@click.group()
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

cli = click.CommandCollection(sources=[warmup, workout])

if __name__ == '__main__':
    cli()
