def filter_solutions():

    with open("solutions.csv") as file:
        content = file.read()

        lista_str = content.split("\n")   # ['Kirka;79-15;22', 'Taina;84-24;60',
        
        lista_op = [] # lista de listas. [['Kirka', '79-15', '22'], ['Taina', '84-24', '60'],

        for string in lista_str:
            if string != "" and string != " ": 
                lista = string.split(";")
                lista_op.append(lista)

        lista_correcto = []  # [['Taina', '84-24', '60'], 
        lista_incorrecto = []  # [['Kirka', '79-15', '22'], ['Kirsi', '86-22', '32'],

        for lista in lista_op:
            operacion = lista[1]
            operacion_mas = lista[1].split("+")
            if len(operacion_mas) == 1: # si tiene un solo elemento, split no encontro el +,
                                        # significa que es una resta
                operacion_resta = lista[1].split("-")
                operacion_res = int(operacion_resta[0]) - int(operacion_resta[1]) # calcula la operacion
                if operacion_res == int(lista[2]):  # si el resultado real coincide con el del texto, se graba
                    lista_correcto.append(lista)
                else:
                    lista_incorrecto.append(lista)
            elif len(operacion_mas) != 1: # significa que split funciono y es una suma
                operacion_suma = lista[1].split("+")  
                operacion_res = int(operacion_suma[0]) + int(operacion_suma[1]) # calcula la operacion    
                if operacion_res == int(lista[2]):
                    lista_correcto.append(lista)
                else:
                    lista_incorrecto.append(lista)


    with open("correct.csv", "w") as my_file:
        
        for lista in lista_correcto:
            line = f"{lista[0]};{lista[1]};{lista[2]}"
            my_file.write(line+"\n")

    with open("incorrect.csv", "w") as my_file:
      
        for lista in lista_incorrecto:
            line = f"{lista[0]};{lista[1]};{lista[2]}"
            my_file.write(line+"\n")        


                   
if __name__ == "__main__":

    filter_solutions()        