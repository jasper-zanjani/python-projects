import json
import csv
import click
import glob
import os.path

def read(filename):
    output = list()
    with open(filename,'r') as f:
        cr = csv.reader(f)
        headers = next(cr)
        for i in cr:
            output.append(dict(zip(headers,next(cr))))
        print(f'{filename} read')
    return output

def write(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f)
        print(f'{filename} written')

@click.command()
@click.argument('filename', nargs=-1)
def main(filename):
    print(f"Received argument {filename}")
    files = list()

    if isinstance(filename,str):
        if filename[0].find( '*') > 0:
            print('Initiating globbing')
            files = [os.path.abspath(f) for f in glob.glob(os.path.expanduser(filename[0]))]
        else:
            files = list(filename[0])
    else:
        files = [i for i in filename]

    print(f'Converting {len(files)} files ')
    for f in files:
        data = read(f)
        output_filename = f.replace('csv','json')
        write(data,output_filename)

if __name__ == '__main__':
    main()
