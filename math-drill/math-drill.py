import random
# from colorama import colorama.Fore, Back, colorama.Style
import colorama
from enum import Enum

class Operations(Enum):
    ADDITION = 'Addition'
    SUBTRACTION = 'Subtraction'

def print_equation(*ops, operation=Operations.ADDITION, streak=0):
    if operation == Operations.ADDITION:
        print(colorama.Fore.CYAN,str(ops[0]), end='')
        print(colorama.Style.RESET_ALL,' + ', end='')
        print(colorama.Fore.YELLOW,str(ops[1]), end='')
        answer = ops[0] + ops[1]
    elif operation == Operations.SUBTRACTION:
        print(colorama.Fore.CYAN,str(ops[1]), end='')
        print(colorama.Style.RESET_ALL,' - ', end='')
        print(colorama.Fore.YELLOW,str(ops[0]), end='')
        answer = ops[1] - ops[0]
    else:
        print(colorama.Fore.RED, "Unknown operation!")
    print(colorama.Style.RESET_ALL,' = ', end='')
    # print(f"{a} + {b} = ", end="")
    c = input()
    if str(answer) == c:
        print(colorama.Fore.GREEN, 'Correct!',end='')
        if streak > 5:
            print(colorama.Fore.CYAN, colorama.Style.BRIGHT,f' STREAK: {streak}', end='')
        print(colorama.Style.RESET_ALL, end='\n\n')
        return True
    else:
        print(colorama.Fore.RED, 'Incorrect! ', end='')
        print(colorama.Style.RESET_ALL, 'Try again, Smellyana...', end='\n\n')
        return False

def main():
    try:
        colorama.init()
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
        exit() 

if __name__ == '__main__':
    main() 
