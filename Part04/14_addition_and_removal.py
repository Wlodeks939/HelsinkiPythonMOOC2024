# Write your solution here

list = []

print(f"The list is now {list}")

i = 1
inp = 'a'

while True:

    inp = input("a(d)d, (r)emove or e(x)it:")
    if inp == "d":
        list.append(i)
        print(f"The list is now {list}")
        i += 1 
    elif inp == "r" and len(list) >= 1:
        list.pop()  
        print(f"The list is now {list}")
        i -= 1 
    elif inp == "x":
        print("Bye!")
        break     

