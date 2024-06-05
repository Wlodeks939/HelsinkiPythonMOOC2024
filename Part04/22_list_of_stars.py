# Write your solution here

def list_of_stars(lista):

    for i in range(len(lista)):
        print("*" * int(lista[i]))


if __name__ == "__main__":

    list_of_stars([3, 7, 1, 1, 2])        