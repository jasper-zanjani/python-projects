import colorama
import emoji
from .Operations import Operations

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
    c = input()
    if str(answer) == c:
        print(colorama.Fore.GREEN, 'Correct!',end='')
        if streak > 1:
            print(colorama.Fore.CYAN, colorama.Style.BRIGHT,f' STREAK: {streak} ', end='')
            if streak > 19: print(emoji.emojize(':unicorn:'))
        print(colorama.Style.RESET_ALL, end='\n\n')
        return True
    else:
        print(colorama.Fore.RED, 'Incorrect! ', end='')
        print(colorama.Style.RESET_ALL, 'Try again, Smellyana...', end='\n\n')
        return False
