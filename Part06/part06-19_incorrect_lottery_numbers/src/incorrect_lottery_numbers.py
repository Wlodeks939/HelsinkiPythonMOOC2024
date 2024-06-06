def filter_incorrect():

    with open("lottery_numbers.csv") as file:
        
        lista_str = file.read().split("\n") # ['week 1;17,19,35,23,8,20,36', 'week 2;24,28,35,8,3,22',

        # creo diccionario, key es week y value es una lista con un string con los numeros

        dic = {} # {'week 1': '17,19,35,23,8,20,36', 'week 2': '24,28,35,8,3,22',

        for str in lista_str:
            if ";" in str:
                x = str.split(";")  # ['week 1', '17,19,35,23,8,20,36']
                
                dic[x[0]] = x[1]  # x[1] : 17,19,35,23,8,20,36   <class 'str'>
                
            

        # creo diccionario2, key es week y value es una lista de numeros en formato string
                
        dic2 = {} # {'week 1': ['17', '19', '35', '23', '8', '20', '36'],

        for key,value in dic.items():
    
            dic2[key] = value.split(",")  # value es un string, ej '17,19,35,23,8,20,36'
            

        # creo diccionario3, convierte a entero los numeros e ignora las semanas que tienen numeros y letras

        dic3 = {}  # {'week 1': [17, 19, 35, 23, 8, 20, 36],
                    # Ej: ignora week 8;32,21,26,1,15aa,14,17 
                    # Tambien filtra numeros menores a 1 o mayores a 39 

        for key,value in dic2.items():
            try:
                lista = []
                for j in range(len(value)):
                    if int(value[j]) >= 1 and int(value[j]) <= 39:
                        lista.append(int(value[j]))
                dic3[key] = lista    
            except:
                pass  

               

        dic4 = {} # filtra semanas que no tienen exactamente 7 numeros

        for key,value in dic3.items():
            if len(value) == 7:
                dic4[key] = value


        dic5 = {} # Filtra las semanas mal escritas. Ej week x
                  # {'week 1': [17, 19, 35, 23, 8, 20, 36], 'week 4': [21, 2, 22, 14, 4, 28, 38]

        for key,value in dic4.items():
            string = key
            week, num = string.split(" ")
            if num.isdigit():
                dic5[key] = value

        dic6 = {} # filtra las semanas con numeros duplicados  

        dup = False
        for key,value in dic5.items():
            lista_sorted = sorted(value)  
            for j in range(6):
                if  lista_sorted[j] == lista_sorted[j+1]:
                    dup = True 
                    break
            if not dup:
                dic6[key] = value    

    with open("correct_numbers.csv", "w") as my_file:

        for key,value in dic6.items():
            line = f"{key};{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}"
            my_file.write(line+"\n")

if __name__ == "__main__":

    filter_incorrect()    