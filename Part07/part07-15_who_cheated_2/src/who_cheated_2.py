import csv
from datetime import datetime, timedelta



def final_points():

    # crea dict con key = name y value = objeto datetime
    students_inicial = {}  #  {'matti': datetime.datetime(1900, 1, 1, 13, 33),

    # strptime crea un objeto datetime. Primer argumento el string, segundo argumento tenes que decirle
    # que info contiene ese string.


    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=';'):
            student = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")
            students_inicial[student] = start_time

    

    students_final = {}   

    # crea diccionario de diccionarios. Porque si usamos diccionario con key y value siendo una lista,
    # como el diccioario no puede tener llaves duplicadas, cuando venga una nueva tarea va a sobreescribir
    # el valor que tenga y no va a contemplar todas las tareas

    # Cada estudiante tiene un diccionario de tareas

    # {'arto': {'1': ('0', datetime.datetime(1900, 1, 1, 20, 4)), '5': ('3', datetime.datetime(1900, 1, 1, 18, 19)),

    with open("submissions.csv") as file:  # name;task;points;hh:mm
        for line in csv.reader(file, delimiter=';'):
            student = line[0]
            task = line[1]
            points = int(line[2])
            finish_time = datetime.strptime(line[3], "%H:%M")
            
            start_time_temp = students_inicial[student]
            time_elapsed = finish_time - start_time_temp 

            if time_elapsed < timedelta(hours=3):
                if student not in students_final: #crea un diccionario para cada estudiante
                    students_final[student] = {}

        
                #popula diccionario con las tareas pero ignora las que tardaron mas de 3 horas
                if task not in students_final[student]:
                    students_final[student][task] = (points,finish_time)

                if task in students_final[student]: 

                    if points > students_final[student][task][0]:
                        students_final[student][task] = (points,finish_time)
                        # accedes a la llave task del diccionario que esta en la llave student

    

    student_finalpoints = {}

    for name,dict_tasks in students_final.items():

        suma = 0
        for task,value in dict_tasks.items():
            suma += int(value[0])

        student_finalpoints[name] = suma



    return student_finalpoints

if __name__ == "__main__":

    print(final_points())