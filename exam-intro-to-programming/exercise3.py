def read_points():

    with open("exercise3.txt") as file:
        content = file.read()

    lista_str = content.split("\n")   # ['Heba hawks:5-6-1', 'Brewsters:3-12-10',
    
    dic = {} # {'Heba hawks': '5-6-1', 'Brewsters': '3-12-10',

    for string in lista_str:
        temp = string.split(":")
        dic[temp[0]] = temp[1]

    
    try:
        for key,value in dic.items():  # {'Heba hawks': 21, 'Brewsters': 21,
            
            points = 0
            temp = value.split("-")  
            points = int(temp[0])*3 + int(temp[1])
            dic[key] = points 

    except ValueError:
        print("Invalid format in file: [20]")
        return

    list_results = []  # [('Heba hawks', 21), ('Brewsters', 21),

    for key,value in dic.items():
        tupla = (key,value)
        list_results.append(tupla)

    return list_results     

print(read_points())  