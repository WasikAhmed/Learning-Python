def factorial(n):
    if n == 0:
        return 1

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(3))
    print(factorial(5))
    print(factorial(10))