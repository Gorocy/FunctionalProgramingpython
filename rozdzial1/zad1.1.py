def main():
    Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Lista : ", Lista ,".", sep="")

    sum = 0

    for i in Lista:
        sum = i + sum
    print("Suma listy wynosi: ", sum, sep="")

main()