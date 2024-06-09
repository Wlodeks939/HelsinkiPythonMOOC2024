def most_common_words(filename: str, lower_limit: int):

    with open(filename) as file:

        contenido = file.read() #string type
        contenido = contenido.replace(","," ").replace("."," ").replace("’"," ").replace('"'," ")
        contenido = contenido.replace("("," ").replace(")"," ").replace("'"," ").replace("_"," ")
        contenido = contenido.split()


    dic = {}
    for word in contenido:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1 

    dic2 = {}         

    for key,value in dic.items():
        if value >= lower_limit:
            dic2[key] = value

    return dic2         

if __name__ == "__main__":
    print(most_common_words("programming.txt", 6))