def main():
    N =10
    macierz1= [[1 for i in range(N)] for j in range(N)]

    macierz2 = [[2 for i in range(N)] for j in range(N)]

    macierz3 = [[0 for i in range(N)] for j in range(N)]


    for i in range(N):
        for j in range(N):
            print(macierz1[i][j], " ", end="")

        print()
    print()

    for i in range(N):
        for j in range(N):
            print(macierz2[i][j], " ", end="")

        print()
    print()


    for i in range(N):
        for j in range(N):
            macierz3[i][j] = macierz2[i][j] + macierz1[i][j]
            print(macierz3[i][j], " ", end="")

        print()
    print()

main()