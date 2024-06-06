import csv
from datetime import datetime, timedelta



def cheaters():

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
            points = line[2]
            finish_time = datetime.strptime(line[3], "%H:%M")
            
            if student not in students_final: #crea un diccionario para cada estudiante
                students_final[student] = {}

            if task not in students_final[student]:
                students_final[student][task] = (points,finish_time)

            if task in students_final[student]: # para que quede la tarea que fue entregada ultima
                if finish_time > students_final[student][task][1]:
                    students_final[student][task] = (points,finish_time)


    

    lista_cheat = []
    for key,dict_tasks in students_final.items():

        start_time_temp = students_inicial[key]
        for task,value in dict_tasks.items():
            finish_time_temp = value[1]
            time_elapsed = finish_time_temp - start_time_temp
            
            if time_elapsed > timedelta(hours=3)  and key not in lista_cheat:
                lista_cheat.append(key)

    return lista_cheat

if __name__ == "__main__":

    print(cheaters())

