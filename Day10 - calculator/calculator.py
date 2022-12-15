#!/usr/local/bin/python

import calculator_art

print(calculator_art.logo)

####################################
def calculate(f_number,operation,l_number):
    if operation == '+':
        return f_number + l_number
    elif operation == '-':
        return f_number - l_number
    elif operation == '*':
        return f_number * l_number
    elif operation == '/':
        return f_number / l_number
#####################################

run_again = True
first_number = input("What's the first number?: ")
while run_again == True:
    list_operations = ['+','-','*','/']
    for item in list_operations:
        print(item)
    operations = input('Pick an operation: ')
    next_number = input("What's the next number?: ")
    result = calculate(float(first_number),operations,float(next_number))
    print(f'{first_number} {operations} {next_number} = {result} ')
    continue_run = input(f"Type 'y' to continue  calculating with {result}, ir type 'n' to start a new calculation: ").lower()
    if continue_run == 'y' or continue_run == 'yes':
        first_number = result
    else:
        run_again = False



