while True:

    print("1 - add an entry, 2 - read entries, 0 - quit")
    entrada = int(input("Function: "))
    

    if entrada == 1:

        entry = input("Diary entry: ")

        with open("diary.txt", "a") as my_file:
            my_file.write(f"{entry}\n")

        print("Diary saved")   

    elif entrada == 2:

        print("Entries:") 

        with open("diary.txt") as file:
            content = file.read()    

            lista_str = content.split("\n")

        for line in lista_str:
            print(line)  

    elif entrada == 0:  
        print("Bye now!")    
        break    