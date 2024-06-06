student = input("Student information:")
exercises = input("Exercises completed:")

#student = "students1.csv"
#exercises = "exercises1.csv"

with open(student) as file:
        content = file.read()

lista_str = content.split()

dict_students = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_students[x[0]] = x[1:]  # populo el diccionario, el primer elemento de x es la llave,
                                      # el resto de los elementos sera el value del diccionario como una lista


with open(exercises) as file:
        content = file.read()

lista_str = content.split()

dict_exer = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_exer[x[0]] = x[1:]        



for key,value in dict_students.items():
        if key in dict_exer and key != "id":
                nombre = dict_students[key]  # es una lista con dos elementos (str). Nombre y apellido
                notas = dict_exer[key]  # es una lista de strings con las notas
                suma = 0
                for nota in notas:
                        suma += int(nota) # itera sobre la lista de strings, convierte a int y suma el total
                
                              
                print(f"{nombre[0]} {nombre[1]} {suma}")
        
#print(dict_students)
#print(dict_exer)        