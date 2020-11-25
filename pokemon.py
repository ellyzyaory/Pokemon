import re

def children_game(file):
    data = open(file, 'r')
    myfile = re.findall("\w+", data.read())
    lst = []

    one = input("Child 1: ")
    if one in myfile:
        lst.append(one)
        two = input("Child 2: ")
    else:
        return False
    while True:
        if two in myfile and one[-1] == two[0] and two not in lst:
            lst.append(two)
            one = input("Child 1: ")
        else:
            return False
        if one in myfile and two[-1] == one[0] and one not in lst:
            lst.append(one)
            two = input("Child 2: ")
        else:
            return False

if __name__ == "__main__":
    print(children_game("pokemon.txt"))
