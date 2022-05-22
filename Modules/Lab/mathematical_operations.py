def perform_operation(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            raise ValueError('Number 2 must not be equal to zero')
        return number1 / number2
    elif operation == '^':
        return number1 ** number2
    else:
        raise ValueError('Operation must be one of the following: "+", "-", "*", "/", "^",')

print(perform_operation(1.23, 2, '+'))
