import json

def print_persons(filename: str):

    with open(filename) as my_file:
        data = my_file.read()

    students = json.loads(data)
    



    for student in students:

        if len(student["hobbies"]) == 0:
            hobbies_string2 = "()"
        else:    
            hobbies_string = "("
            for str in student["hobbies"]:  #  crea esto:  (coding, rock climbing, reading)
                hobbies_string += f"{str}, "
            n = len(hobbies_string) 
            hobbies_string2 = hobbies_string[:n-2] # saca la ultima coma
            hobbies_string2 += ")"
        
        print(f"{student["name"]} {student["age"]} years {hobbies_string2}")