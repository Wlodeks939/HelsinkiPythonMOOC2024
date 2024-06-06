student = input("Student information:")
exercises = input("Exercises completed:")
exam_points = input("Exam points:")

#student = "students1.csv"
#exercises = "exercises1.csv"
#exam_points = "exam_points1.csv"

# creo dict students
with open(student) as file:
        content = file.read()

lista_str = content.split()

dict_students = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_students[x[0]] = x[1:]  # populo el diccionario, el primer elemento de x es la llave,
                                      # el resto de los elementos sera el value del diccionario como una lista

del dict_students["id"]




# creo dict exercises
with open(exercises) as file:
        content = file.read()

lista_str = content.split()

dict_exer = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_exer[x[0]] = x[1:]        

del dict_exer["id"]

# creo nuevo dict que guarda key el id y value la suma de los exercises
dict_exer2 = {}

for key,value in dict_exer.items():
        suma = 0
        for num_str in value:
            suma += int(num_str)
        dict_exer2[key] = suma    

# creo nuevo dict que guarda key el id y value los 'exercise points'
# 10 % of the total exercices awards 1 point, completing at least 20 % awards 2 points, etc.        
dict_exer3 = {}    

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
                                                             
                




# creo dict exam points
with open(exam_points) as file:
        content = file.read()

lista_str = content.split()

dict_exam_points = {}

for item in lista_str:
        x = item.split(";")  # lista_str es una lista de strings. Separo cada string usando ; como separador
        dict_exam_points[x[0]] = x[1:]        

del dict_exam_points["id"]

# creo nuevo dict que guarda key el id y value la suma de los exercises
dict_exam_points2 = {}

for key,value in dict_exam_points.items():
        suma = 0
        for num_str in value:
            suma += int(num_str)
        dict_exam_points2[key] = suma   





# creo nuevo dict que suma 'exercise points' con exam points
        
dict_total_points = {}      

for key,value in dict_exer3.items():
       dict_total_points[key] = dict_exer3[key] + dict_exam_points2[key]
       

# crea nuevo dict con el grade final
       
dict_grades = {}   

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
dict_students2 = {}

for key,value in dict_students.items():
    nombre = f"{value[0]} {value[1]}"
    dict_students2[key] = nombre
      

#print(dict_students)
#print(dict_grades)
#print(dict_students2)


print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")  
for key,value in dict_students2.items():
      nombre = dict_students2[key] # es una lista con dos elementos str
      print(f"{dict_students2[key]:30}{dict_exer2[key]:<10}{dict_exer3[key]:<10}{dict_exam_points2[key]:<10}{dict_total_points[key]:<10}{dict_grades[key]:<10}")