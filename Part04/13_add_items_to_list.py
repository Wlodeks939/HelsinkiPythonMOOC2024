# Write your solution here

n = int(input("How many times:"))
list = []
i = 1

while n > 0:

    num = int(input(f"Item {i}:"))
    list.append(num)
    n -= 1
    i += 1
print(list)    
