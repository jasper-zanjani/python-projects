import click


@click.command()
@click.option('--weather',
              prompt="How is the weather where you are?",
              type=click.Choice(['sunny', 'overcast', 'rainy']),
              required=True)
def weather(weather):
    print(f'I love it when it is {weather}...')


if __name__ == '__main__':
    weather()
