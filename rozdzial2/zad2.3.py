def main():
    lista1 = [1, 3, 5, 7, 9]
    lista2 = [2, 4, 6, 8, 10]

    lista3 = lista1 + lista2
    lista4 = lista2 + lista1

    print("lista1  = ", lista1, "lista2 = ", lista2, sep="")
    print("lista2  = ", lista2, "lista1 = ", lista1, sep="")

    print("lista1  + lista2 = ", lista3, sep="")
    print("lista2  + lista1 = ", lista4, sep="")


main()