def main():
    n1 = 0
    n2 = 1
    n = 0
    k = int(input("do ktorej liczby ciagu fibonacciego policzyc: "))

    if k == 1:
        print("Dla: ", k, " elementu wynosi; ", n1, sep="")
        return
    if k == 2:
        print("Dla: ", k, " elementu wynosi; ", n2, sep="")
        return
    k = k - 2

    for i in range(k):
        n = n1 + n2
        n1 = n2
        n2 = n
    print("Dla: ", k, " elementu wynosi; ", n, sep="")


main()
