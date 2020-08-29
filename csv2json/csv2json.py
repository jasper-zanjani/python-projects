import json
import csv
import click

def read(filename):
    output = list()
    with open(filename,'r') as f:
        cr = csv.reader(f)
        headers = next(cr)
        output.append(dict(zip(headers,next(cr))))
    return output

def write(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f)

@click.command()
@click.argument('filename')
def main(filename):
    data = read(filename)
    output_filename = filename.replace('csv','json')
    write(data,output_filename)

if __name__ == '__main__':
    main()
