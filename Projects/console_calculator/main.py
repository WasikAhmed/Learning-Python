def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y


def showOptions():
    print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit')
    choice = int(input('Please choose an option: '))
    return choice


def take_input():
    x = int(input('Please enter 1st number: '))
    y = int(input('Please enter 2nd number: '))
    return x, y


print('Welcome to the Calculator!!!')
while True:
    option = showOptions()
    if option == 5:
        print('Thank you for using my calculator!!!')
        break
    x, y = take_input()
    if option == 1:
        result = add(x, y)
        print("Sum of {} and {} is {}".format(x, y, result))
    elif option == 2:
        result = sub(x, y)
        print("Subtraction of {} and {} is {}".format(x, y, result))
    elif option == 3:
        result = mul(x, y)
        print("Multiplication of {} and {} is {}".format(x, y, result))
    elif option == 4:
        result = div(x, y)
        print("Division of {} and {} is {}".format(x, y, result))
