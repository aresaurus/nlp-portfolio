# Operation functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: cannot divide by zero"
    return n1 / n2

# Looks up the operation in the dictionary and applies it to n1 and n2
def calculation(n1, n2, operation, operations_dict):
    if operation not in operations_dict:
        return "Error: invalid operation"
    return operations_dict[operation](n1, n2)

# Dictionary to store the different operations
operations = {'+' : add,
              '-' : subtract,
              '*' : multiply,
              '/' : divide}

should_continue = True
keep_first_number = ''

while should_continue:
    first_number = float(input('Please enter your first number: '))
    chosen_operation = input(
        'What do you want to do with that number?\nType "+" for addition,"-" for subtraction, "*" for multiplication and "/" for division: ')
    second_number = float(input('Please enter your second number: '))
    result = calculation(first_number, second_number, chosen_operation, operations)
    print(f'The result is: {result}')

    keep_calculating = input('Do you want to do another operation?\n'
                             'Type "yes" to continue, "no" to exit: ')

    if keep_calculating == 'yes':
        keep_first_number = input('Do you want to operate on your previous result?\n'
                                  'Type "yes" or "no": ')
        if keep_first_number == "yes":
            first_number = result
        else:
            first_number = float(input('Please enter your first number: '))

        chosen_operation = input(
            'What do you want to do with that number?\nType "+" for addition,"-" for subtraction, "*" for multiplication and "/" for division: ')
        second_number = float(input('Please enter your second number: '))
        result = calculation(first_number, second_number, chosen_operation, operations)

        print(f'The result is: {result}')

    else:
        should_continue = False
        print('Goodbye!')