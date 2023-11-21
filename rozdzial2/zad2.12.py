import random

def main():
    lista = list(range(1, 101))




    print("lista zawiera", lista, ".", sep="")
    a=0
    for i in range(100):
        a=a+lista[i-1]
    print("suma wynosi : ", a)



main()

