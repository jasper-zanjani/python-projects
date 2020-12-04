import random
import colorama
import sys

from .print_equation import print_equation
from .Operations import Operations

def main():
    try:
        correct = True
        streak=0
        while True:
            if correct == True:
                streak += 1
                b = random.randrange(10)
                a = random.randrange(b,20)
                op = random.sample(list(Operations), 1)[0]
            elif correct == False:
                streak = 0
            correct = print_equation(b,a,operation=op, streak=streak)
    except KeyboardInterrupt:
        print('\n')
        sys.exit()
