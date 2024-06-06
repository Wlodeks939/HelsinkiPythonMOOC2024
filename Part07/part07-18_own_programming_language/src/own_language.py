from string import ascii_uppercase

def run(program):

    # creacion de un dict de variables y se inician a 0: {'A': 0, 'B': 0, 'C': 0,
    variables = {}
    for letter in ascii_uppercase:
        variables[letter] = 0


    to_print = []

    # popula una lista con las location
    locations = []
    for i in range(len(program)):
        if ":" in program[i]:
            location_parts = program[i].split(":")
            location = (i,location_parts[0])
            locations.append(location)


    i = 0
    
    while i < len(program):

        parts_line = program[i].split()    # ['MOV', 'A', '1']
       

        # part 1: MOV PRINT ADD SUB MUL END
        if parts_line[0] == "MOV":
            if parts_line[2].isdigit():
                variables[parts_line[1]] = int(parts_line[2]) # asigna el valor a la variable {'A': '1', 'B': '2',
            else:
                variables[parts_line[1]] = variables[parts_line[2]]
        if parts_line[0] == "PRINT":  
            if parts_line[1].isdigit():
                to_print.append(int(parts_line[1]))
            else:    
                to_print.append(int(variables[parts_line[1]]))  # [1, 2]
        if parts_line[0] == "ADD":  
            if parts_line[2].isdigit():
                variables[parts_line[1]] += int(parts_line[2])
            else:
                variables[parts_line[1]] += variables[parts_line[2]]
        if parts_line[0] == "SUB":  
            if parts_line[2].isdigit():
                variables[parts_line[1]] -= int(parts_line[2])
            else:
                variables[parts_line[1]] -= variables[parts_line[2]]     
        if parts_line[0] == "MUL":  
            if parts_line[2].isdigit():
                variables[parts_line[1]] *= int(parts_line[2])
            else:
                variables[parts_line[1]] *= variables[parts_line[2]] 
        if parts_line[0] == "END": 

            return to_print      
        
        # part 2 JUMP IF JUMP

        if parts_line[0] == "JUMP":    
            goto_location = parts_line[1]  # ("JUMP begin")
            for loc in locations:
                if goto_location == loc[1]:
                    i = loc[0] 

        if "IF" in program[i]:  
            condition_string = parts_line[1:4]  # agarra elementos 1 a 3 ['IF', 'A', '>=', 'B', 'JUMP', 'quit']       
            if condition_string[0].isdigit():
                value1 = int(condition_string[0]) 
            else:
                value1 = variables[condition_string[0]]        # condition_string[0] :  'A'        
            if condition_string[2].isdigit():
                value2 = int(condition_string[2]) 
            else:
                value2 = variables[condition_string[2]]  
            if condition_string[1]  == ">":
                if value1 > value2:
                    goto_location = parts_line[5] # elemento 5 de: "IF A >= B JUMP quit"  quit
                    for loc in locations:
                        if goto_location == loc[1]:
                            i = loc[0] 
            elif condition_string[1]  == ">=":
                if value1 >= value2:
                    goto_location = parts_line[5] # elemento 5 de: "IF A >= B JUMP quit"  quit
                    for loc in locations:
                        if goto_location == loc[1]:
                            i = loc[0]
            elif condition_string[1]  == "<":
                if value1 < value2:
                    goto_location = parts_line[5] # elemento 5 de: "IF A >= B JUMP quit"  quit
                    for loc in locations:
                        if goto_location == loc[1]:
                            i = loc[0]  
            elif condition_string[1]  == "<=":
                if value1 <= value2:
                    goto_location = parts_line[5] # elemento 5 de: "IF A >= B JUMP quit"  quit
                    for loc in locations:
                        if goto_location == loc[1]:
                            i = loc[0]  
            elif condition_string[1]  == "==":
                if value1 == value2:
                    goto_location = parts_line[5] # elemento 5 de: "IF A >= B JUMP quit"  quit
                    for loc in locations:
                        if goto_location == loc[1]:
                            i = loc[0]
            elif condition_string[1]  == "!=":
                if value1 != value2:
                    goto_location = parts_line[5] # elemento 5 de: "IF A >= B JUMP quit"  quit
                    for loc in locations:
                        if goto_location == loc[1]:
                            i = loc[0]                                                               

        i += 1

    return to_print

if __name__ == "__main__":

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
  
    print(run(program2))