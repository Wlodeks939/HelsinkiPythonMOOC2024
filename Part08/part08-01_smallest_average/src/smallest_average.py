def smallest_average(person1: dict, person2: dict, person3: dict):

    avg_1 = 0
    avg_2 = 0
    avg_3 = 0
    suma1 = 0
    suma2 = 0
    suma3 = 0

    for key,value in person1.items():

        if key == "name":
            continue
        suma1 += int(person1[key])      
    avg_1 = suma1/3

    for key,value in person2.items():

        if key == "name":
            continue
        suma2 += int(person2[key])      
    avg_2 = suma2/3

    for key,value in person3.items():

        if key == "name":
            continue
        suma3 += int(person3[key])      
    avg_3 = suma3/3

    if avg_1 < avg_2 and avg_1 < avg_3:
        return person1
    elif avg_2 < avg_1 and avg_2 < avg_3:
        return person2
    else:
        return person3


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))