import random
from colorama import Fore, Back, Style
from enum import Enum

class Operations(Enum):
    ADDITION = 'Addition'
    SUBTRACTION = 'Subtraction'

def print_equation(*ops, operation=Operations.ADDITION):
    if operation == Operations.ADDITION:
        print(Fore.CYAN,str(ops[0]), end='')
        print(Style.RESET_ALL,' + ', end='')
        print(Fore.YELLOW,str(ops[1]), end='')
        answer = ops[0] + ops[1]
    else:
        print(Fore.CYAN,str(ops[1]), end='')
        print(Style.RESET_ALL,' - ', end='')
        print(Fore.YELLOW,str(ops[0]), end='')
        answer = ops[1] - ops[0]
    print(Style.RESET_ALL,' = ', end='')
    # print(f"{a} + {b} = ", end="")
    c = input()
    if str(answer) == c:
        print(Fore.GREEN, 'Correct!', Style.RESET_ALL, end='\n\n')
    else:
        print(Fore.RED, 'Incorrect!', Style.RESET_ALL, end='\n\n')

try:
    while True:
        b = random.randrange(10)
        a = random.randrange(b,20)
        op = random.sample(list(Operations), 1)[0]
        print_equation(b,a,operation=op)
        # print(Style.DIM, op.name, end='\n')
        # print(Fore.CYAN,str(a), end='')
        # print(Style.RESET_ALL,' + ', end='')
        # print(Fore.YELLOW,str(b), end='')
        # print(Style.RESET_ALL,' = ', end='')
        # # print(f"{a} + {b} = ", end="")
        # c = input()
        # if str(a + b) == c:
        #     print(Fore.GREEN, 'Correct!', Style.RESET_ALL, end='\n\n')
        # else:
        #     print(Fore.RED, 'Incorrect!', Style.RESET_ALL, end='\n\n')
except KeyboardInterrupt:
    print('\n')
    exit()




