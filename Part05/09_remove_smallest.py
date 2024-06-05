def remove_smallest(numbers: list):
    min = max(numbers) # busca el numero mas grande
    indice = 0 # inicia variable

    #busqueda del minimo y grabado del indice donde esta el minimo
    for i in range(len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
            indice = i

    numbers.pop(indice)



if __name__ == "__main__":
    numbers = [10, 13, 15, 9, 11, 12, 14]
    remove_smallest(numbers)
    print(numbers)            