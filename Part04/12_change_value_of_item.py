# Write your solution here

list = [1, 2, 3, 4, 5]
index = 0

while index != -1:

    index = int(input("Index:"))
    if index == -1:
        break
    New = int(input("New Value:"))

    list[index] = New

    print(list)