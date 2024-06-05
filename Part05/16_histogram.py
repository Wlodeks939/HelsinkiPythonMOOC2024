def histogram(string):

    d = {}

    for char in string:

        if char not in d:
            d[char] = 0
        d[char] += 1

    for key,value in d.items():
        print(f"{key} {value * "*"}")   


   