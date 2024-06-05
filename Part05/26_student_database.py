# la base de datos va a ser un diccionario 
# llave el nombre y value una lista de cursos. Cada curso es una tupla. Es una lista de tuplas
# Inicialmente  se asigna a value el valor "" y dsp se le cambia por una lista vacia y luego
# se agregan cursos a la lista vacia


def add_student(database: dict,name:str):

    database.update({name: ""})


def print_student(database,name):

    if name in database:
        if database[name] == "":
            print(f"{name}:")    
            print(" no completed courses")
        else:
            print(f"{name}:") 
            print(f" {len(database[name])} completed courses:")  # database[name] es la lista de cursos
            for j in range(len(database[name])):
                lista = database[name]
                print(f"  {lista[j][0]} {lista[j][1]}")  # printea el 1er elemento de la tupla y dsp el 2do
            # calculo promedio
            suma_cursos = 0
            for j in range(len(database[name])):
                suma_cursos += lista[j][1]     
            avg = suma_cursos/(len(database[name]))
            print(f" average grade {avg}")


    if name not in database:
        print(f"{name}: no such person in the database")  

def add_course(database,name,course: tuple):

    course_name, grade = course  # crea variables para cada elemento de la tupla

    # filtra los cursos con nota 0
    if grade > 0:
        # se crea una lista vacia para poner los cursos en el caso de que no tenga cursos ya hechos
        if database[name] == "":
            database[name] = []

        lista_nombres_cursos = []  # helper. Lista con los nombres de los cursos
        for stored_course in database[name]:
            lista_nombres_cursos.append(stored_course[0]) # popula la lista

        # agrega si no esta en la lista, si ya esta en la lista no lo agrega
        if course_name not in lista_nombres_cursos:
            database[name].append(course)

        # si ya esta en la lista pero el grade es mayor, se elimina el curso con menor nota y 
        # se agrega el de mayor nota
        if course_name in lista_nombres_cursos:
            for curso in database[name]: # curso es una tupla con dos valores, nombre y grade
                if course_name == curso[0] and grade > curso[1]:
                    database[name].remove(curso) # quita al curso con menor grade de la lista
                    database[name].append(course) # agrega el curso de mayor grade a la lista


def summary(database):

    # cantidad estudiantes
    n = len(database)
    print(f"students {n}")

    # most courses completed

    most_courses_completed = "" # nombre del alumno con mas cursos hechos
    most_courses_completed_n = 0 # cantidad de cursos del que mas cursos hizo

    for key,value in database.items(): # recorre el diccionario de estudiantes llave por llave. 
                                       # value es una lista de tuplas con los cursos 
        if len(value)> most_courses_completed_n:
            most_courses_completed_n = len(value)
            most_courses_completed = key

    print(f"most courses completed {most_courses_completed_n} {most_courses_completed}")        

    # best average grade

    best_avg_name = ""
    best_avg = 0
    

    for key,value in database.items():   # value es una lista de tuplas con los cursos
        suma_notas = 0 # reinicia para cada estudiante
        avg = 0
        for j in range(len(value)): # recorro cada lista
            suma_notas += value[j][1]  # accedo al segundo elemento de la tupla j de la lista de tuplas
        avg = suma_notas/(len(value))
        if avg > best_avg:
            best_avg = avg  # actualizo el mejor promedio
            best_avg_name = key # actualizo el nombre del mejor promedio

    print(f"best average grade {best_avg} {best_avg_name}")    




if __name__ == "__main__":


    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    print(students)
    summary(students)