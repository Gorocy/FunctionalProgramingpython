def fibonacci(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    a = 0
    b = 1
    c = 0
    for i in range(n-2):
        c = a + b
        a = b
        b = c

    return c


def main():
    print("20 liczba ciagu fibonacciego: ")

    fib = fibonacci(5)
    print(fib)


main()
