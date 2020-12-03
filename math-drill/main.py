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
    elif operation == Operations.SUBTRACTION:
        print(Fore.CYAN,str(ops[1]), end='')
        print(Style.RESET_ALL,' - ', end='')
        print(Fore.YELLOW,str(ops[0]), end='')
        answer = ops[1] - ops[0]
    else:
        print(Fore.RED, "Unknown operation!")
    print(Style.RESET_ALL,' = ', end='')
    # print(f"{a} + {b} = ", end="")
    c = input()
    if str(answer) == c:
        print(Fore.GREEN, 'Correct!', Style.RESET_ALL, end='\n\n')
        return True
    else:
        print(Fore.RED, 'Incorrect! ', end='')
        print(Style.RESET_ALL, 'Try again, Smellyana...', end='\n\n')
        return False

try:
    continue_ = True
    while True:
        if continue_ == True:
            b = random.randrange(10)
            a = random.randrange(b,20)
            op = random.sample(list(Operations), 1)[0]
        elif continue_ == False:
            pass
        continue_ = print_equation(b,a,operation=op)
except KeyboardInterrupt:
    print('\n')
    exit()




