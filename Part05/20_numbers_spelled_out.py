def dict_of_numbers():

    d = {}

    d[0] = "zero"
    d[1] = "one"
    d[2] = "two"
    d[3] = "three"
    d[4] = "four"
    d[5] = "five"
    d[6] = "six"
    d[7] = "seven"
    d[8] = "eight"
    d[9] = "nine"
    d[10] = "ten"
    d[11] = "eleven"
    d[12] = "twelve"
    d[13] = "thirteen"
    d[14] = "fourteen"
    d[15] = "fifteen"
    d[16] = "sixteen"
    d[17] = "seventeen"
    d[18] = "eighteen"
    d[19] = "nineteen"
    d[20] = "twenty"
    d[30] = "thirty"
    d[40] = "forty"
    d[50] = "fifty"
    d[60] = "sixty"
    d[70] = "seventy"
    d[80] = "eighty"
    d[90] = "ninety"

    # twenty

    for j in range(21,30):
        d[j] = f"{d[20]}-{d[j-20]}"

    #  Thirty

    for j in range(31,40):
        d[j] = f"{d[30]}-{d[j-30]}"  

    # Forty   

    for j in range(41,50):
        d[j] = f"{d[40]}-{d[j-40]}"   


    # 50s

    for j in range(51,60):
        d[j] = f"{d[50]}-{d[j-50]}"   

    # 60s

    for j in range(61,70):
        d[j] = f"{d[60]}-{d[j-60]}"   

    # 70s

    for j in range(71,80):
        d[j] = f"{d[70]}-{d[j-70]}" 

    # 80s

    for j in range(81,90):
        d[j] = f"{d[80]}-{d[j-80]}"   

    # 90s

    for j in range(91,100):
        d[j] = f"{d[90]}-{d[j-90]}"                   




    return d

if __name__ == "__main__":


    print(dict_of_numbers(34))
    print(dict_of_numbers(45))
    print(dict_of_numbers(53))
    print(dict_of_numbers(67))
    print(dict_of_numbers(78))
    print(dict_of_numbers(85))
    print(dict_of_numbers(99))
    