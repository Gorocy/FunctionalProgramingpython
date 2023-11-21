def main():

    N = 10

    lista = [[0 for i in range(N)] for j in range(N) ]

    for i in range(10):
        for j in range(10):

            if (N == j+i+1):
                lista[i][j] = 1
        print(lista[i])

    a = 0
    for i in range(N):
        a = a + lista[i][N-i-1]

    print("suma przekatnej : ", a)

main()