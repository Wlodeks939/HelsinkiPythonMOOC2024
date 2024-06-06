student = input("Student information:")
exercises = input("Exercises completed:")
exam_points = input("Exam points:")
course = input("Course information:")

#student = "students2.csv"
#exercises = "exercises2.csv"
#exam_points = "exam_points2.csv"
#course = "course3.txt"

# creo dict students     {'12345678': ['pekka', 'peloton'], '12345687': ['jaana', 'javanainen'], ...
with open(student) as file:
        content = file.read()

lista_str = content.split()

dict_students = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_students[x[0]] = x[1:]  # populo el diccionario, el primer elemento de x es la llave,
                                      # el resto de los elementos sera el value del diccionario como una lista

del dict_students["id"]




# creo dict exercises   {'12345678': ['4', '1', '1', '4', '5', '2', '4'],
with open(exercises) as file:
        content = file.read()

lista_str = content.split()

dict_exer = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_exer[x[0]] = x[1:]        

del dict_exer["id"]

# creo nuevo dict que guarda key el id y value la suma de los exercises
dict_exer2 = {}  # {'12345678': 21, '12345687': 27, '12345699': 35}

for key,value in dict_exer.items():
        suma = 0
        for num_str in value:
            suma += int(num_str)
        dict_exer2[key] = suma    

# creo nuevo dict que guarda key el id y value los 'exercise points'
# 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc.        
dict_exer3 = {}    # {'12345678': 5, '12345687': 6, '12345699': 8}

for key,value in dict_exer2.items():
       
       percentage = float(value/40*100)
       if 0 <= percentage <= 9:
              dict_exer3[key] = 0
       elif 10 <= percentage <= 19:
              dict_exer3[key] = 1
       elif 20 <= percentage <= 29:
              dict_exer3[key] = 2 
       elif 30 <= percentage <= 39:
              dict_exer3[key] = 3
       elif 40 <= percentage <= 49:
              dict_exer3[key] = 4
       elif 50 <= percentage <= 59:
              dict_exer3[key] = 5 
       elif 60 <= percentage <= 69:
              dict_exer3[key] = 6
       elif 70 <= percentage <= 79:
              dict_exer3[key] = 7
       elif 80 <= percentage <= 89:
              dict_exer3[key] = 8
       elif 90 <= percentage <= 99:
              dict_exer3[key] = 9
       else:
              dict_exer3[key] = 10
                                                             
                




# creo dict exam points  {'12345678': ['4', '1', '4'], '12345687': ['3', '5', '3'], ..
with open(exam_points) as file:
        content = file.read()

lista_str = content.split()

dict_exam_points = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_exam_points[x[0]] = x[1:]        

del dict_exam_points["id"]

# creo nuevo dict que guarda key el id y value la suma de los exercises
dict_exam_points2 = {}   #  {'12345678': 9, '12345687': 11, '12345699': 14}

for key,value in dict_exam_points.items():
        suma = 0
        for num_str in value:
            suma += int(num_str)
        dict_exam_points2[key] = suma   





# creo nuevo dict que suma 'exercise points' con exam points
        
dict_total_points = {}      # {'12345678': 14, '12345687': 17, '12345699': 22}

for key,value in dict_exer3.items():
       dict_total_points[key] = dict_exer3[key] + dict_exam_points2[key]
       

# crea nuevo dict con el grade final
       
dict_grades = {}   # {'12345678': 0, '12345687': 1, '12345699': 3}

for key,value in dict_total_points.items():
    if 0 <= value <= 14:
        dict_grades[key] = 0
    elif 15 <= value <= 17:
        dict_grades[key] = 1
    elif 18 <= value <= 20:
        dict_grades[key] = 2  
    elif 21 <= value <= 23:
        dict_grades[key] = 3
    elif 24 <= value <= 27:
        dict_grades[key] = 4
    else:
        dict_grades[key] = 5              



# crea nuevo dict students donde el value no es una lista de dos strings si no un solo string
        # dict students     {'12345678': ['pekka', 'peloton'], '12345687': ['jaana', 'javanainen'], ...
        # dict students2  {'12345678': 'pekka peloton', '12345687': 'jaana javanainen', '12345699': 'liisa virtanen'}
dict_students2 = {}

for key,value in dict_students.items():
    nombre = f"{value[0]} {value[1]}"
    dict_students2[key] = nombre
      


# crea results.csv

with open("results.csv", "w") as my_file:

    for key,value in dict_students2.items():
          
        line = f"{key};{dict_students2[key]};{dict_grades[key]}"
        my_file.write(line+"\n")


# para crear results.txt primero necesitamos nombre curso y creditos

with open(course) as file:
    content = file.read()

# obtengo name
lista_str = content.split("\n") # ['name: Introduction to Programming', 'study credits: 5']
temp,name = lista_str[0].split(":")
name = name.strip()

#obtengo creditos

temp,credits = lista_str[1].split(":")
credits = credits.strip()




# crea results.txt

with open("results.txt", "w") as my_file:
    line = f"{name}, {credits} credits"
    my_file.write(line+"\n")
    line = "======================================"
    my_file.write(line+"\n")
    line = "name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade"
    my_file.write(line+"\n")
      
    for key,value in dict_students2.items():
        line = f"{dict_students2[key]:30}{dict_exer2[key]:<10}{dict_exer3[key]:<10}{dict_exam_points2[key]:<10}{dict_total_points[key]:<10}{dict_grades[key]:<10}"
        my_file.write(line+"\n")
     

   