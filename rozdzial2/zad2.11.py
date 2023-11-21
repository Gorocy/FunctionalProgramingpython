import random

def main():
    list = []
    for i in range(10):
        list.append(random.randint(1, 100))


    print("lista zawiera", list, ".", sep="")
    print("lista zawiera min= ", min(list))
    print("lista zawiera max= ", max(list))





main()

