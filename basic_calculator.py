arithmeticOperation = {
    'Addition': '+',
    'Subtraction': '-',
    'Multipication': '*',
    'Division': '/',
    'Exponentiation': '**',
}

inputOppList = ['+', '-', '*', '/', '**']

def advancedCalculator(value, inputOpp, value2):
    if inputOpp in inputOppList:
        if inputOpp == '+':
            return value + value2
        if inputOpp == '-':
            if value >= value2:
                return value - value2
            if value2 >= value:
                return value2 - value
        if inputOpp == '*':
            return value * value2
        if inputOpp == '/':
            if value2 != 0:
                return value / value2
            if value2 == 0:
                return "Error: Division by zero is not defined"
        if inputOpp == '**':
            return value ** value2
    else:
        "The calculator is not able to provide an answer."


while True:
    # Prompt the user for input
    print('Enter the input value: ')
    value = int(input())
    print('Enter the input operation (+, -, *, /, **): ')
    inputOpp = input()
    print('Enter the 2nd input value: ')
    value2 = int(input())

    # Convert the  and print the result
    result = int(advancedCalculator(value, inputOpp, value2))
    print(f'{value} {inputOpp} {value2} = {result}')

    # Prompt the user to continue or quit
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break
