def invert(dictionary: dict):

    d2 = {}

    for key,value in dictionary.items():
        d2[value] = key

    dictionary.clear() 

    for key,value in d2.items():
        dictionary[key] = value






if __name__ == "__main__":

    d = {
        "first": 1,
        "second": 2,
        "hola": 4

     }    
    
    print(d)

    invert(d)

    print(d)

   