# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    liczby = list(range(1, 10, 2))

    print("Wygenerowane liczby przez range(1, 10, 2)")

    print(liczby)

    print("Byla ona generowana w nastepujacy sposob")

    for i in liczby:
        print(i)
    print("Dostep do poszczegolnych liczb przez index")
    print()
    index = 0

    while index <len(liczby):
        print("liczby[", index, "]", sep="")
        index+=1
    print()

    print(len(liczby))

main()