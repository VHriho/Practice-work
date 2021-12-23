from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2
from exp_root.root import root3
from logarithm.logarithm import log, lg, ln 
import time

def main():
    print('\n--This is the main function selection menu--\n'
        '1) Factorial\n'
        '2) Exponentiation to square\n'  
        '3) Exponentiation to cube\n'
        '4) Square root\n'  
        '5) Cube root\n'  
        '6) Arbitrary logarithm\n'
        '7) Natural logarithm\n'  
        '8) Decimal logarithm\n')
    s = 'Yes'
    while s:
        w = 1
        while w:
            inpt = input('Enter number of your choise: ')
            if inpt == '1':
                while w:
                    try:
                        num = int(input('Enter a natural number: '))
                        if num > 0:
                            print(f'Your result is: {fact(num)}')
                            w = 0
                        else:
                            raise
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '2':
                while w:
                    try:
                        num = float(input('Enter number: '))
                        print(f'Your result is: {exp2(num)}')
                        w = 0
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '3':
                while w:
                    try:
                        num = float(input('Enter number: '))
                        print(f'Your result is: {exp3(num)}')
                        w = 0
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '4':
                while w:
                    try:
                        num = float(input('Enter a positive number: '))
                        if num > 0:
                            print(f'Your result is: {root2(num)}')
                            w = 0
                        else:
                            raise
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '5':
                while w:
                    try:
                        num = float(input('Enter a positive number: '))
                        if num > 0:
                            print(f'Your result is: {root3(num)}')
                            w = 0
                        else:
                            raise
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '6':
                while w:
                    try:
                        a, b = float(input('Enter a base: ')), float(input('Enter a number: '))
                        if a > 0 and a != 1 and b >0:
                            print(f'Your result is: {log(b, a)}')
                            w = 0
                        else:
                            raise
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '7':
                while w:
                    try:
                        b = float(input('Enter a number: '))
                        if b >0:
                            print(f'Your result is: {ln(b)}')
                            w = 0
                        else:
                            raise
                    except:
                        print('Oops! Not valid value.')
            elif inpt == '8':
                while w:
                    try:
                        b = float(input('Enter a number: '))
                        if b >0:
                            print(f'Your result is: {lg(b)}')
                            w = 0
                        else:
                            raise
                    except:
                        print('Oops! Not valid value.')
            else:
                print('Oops! Choose from 1,2,3,4,5,6,7,8.')
        r = input('Would you like restart program? Enter [Yes] or another key to exit: ')
        if r != 'Yes':
            print('Stop of work...')
            time.sleep(1)
            s = 0
        else:
            print('Restarting...\n')
            continue
if __name__ == '__main__':
    main()