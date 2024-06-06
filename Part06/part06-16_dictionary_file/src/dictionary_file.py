
                
while True:
        
        print("1 - Add word, 2 - Search, 3 - Quit")
        entrada = int(input("Function: "))

        if entrada == 1:
                
                finnish = input("The word in Finnish:")
                english = input("The word in English:")
                
                with open("dictionary.txt", "a") as my_file:

                    line = f"{finnish};{english}"
                    my_file.write(f"{line}\n")
                print("Dictionary entry added")

        elif entrada == 2:   

            with open("dictionary.txt") as file:
        
                lista_str = file.read().split("\n") # ['auto;car', 'roska;garbage']

                dic = {}  # {'auto': 'car', 'roska': 'garbage'}
                for str in lista_str:
                    if str == "" or str == " ":
                         continue
                    key,value = str.split(";")
                    dic[key] = value  # populo el dic

            search_term = input("Search term:")  

            for key,value in dic.items():
                 if search_term in value or search_term in key:
                      print(f"{key} - {value}")    

        elif entrada == 3:   
             print("Bye!")
             break              


