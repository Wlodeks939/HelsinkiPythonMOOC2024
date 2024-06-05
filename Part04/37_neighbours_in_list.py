# Write your solution here

def longest_series_of_neighbours(lista):

    count = 1
    list_max = []

    for i in range(len(lista)-1):

        if lista[i] - lista[i+1] == 1 or lista[i] - lista[i+1] == -1:
            count += 1
        else:
            list_max.append(count)
            count = 1

    list_max.append(count)
    return max(list_max)


if __name__ == "__main__":

    my_list = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
    print(longest_series_of_neighbours(my_list))