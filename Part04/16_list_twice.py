# Write your solution here

lista = []

while True:

    item = int(input("New item: "))

    if item != 0:
        lista.append(item)
        print(f"The list now: {lista}")
        print(f"The list in order: {sorted(lista)}")
    else:
        print("Bye!")    
        break
