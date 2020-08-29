import json
import csv
import click

data = []

@click.command()
@click.argument('filename')
def main(filename):
    with open(filename,'r') as f:
        cr = csv.reader(f)
        headers = next(cr)
        data.append(dict(zip(headers,next(cr))))
    output = filename.replace('csv','json')
    with open(output,'w') as f:
        json.dump(data,f)

if __name__ == '__main__':
    main()
