
d = {}  

while True:

    entrada = int(input("command (1 search, 2 add, 3 quit):"))

    if entrada == 2:
        name = input("name:")
        number = input("number:")
        d[name] = number
        print("ok!")
        

    if entrada == 1:
        name = input("name:")
        if name not in d:
            print("no number")
        else:    
            print(d[name])   

    if entrada == 3:
        print("quitting...")
        break    


if __name__ == "__main__":

    pass