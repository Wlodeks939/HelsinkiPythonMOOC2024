from string import ascii_letters,digits

def change_case(orig_string: str):

    string2 = ""

    for char in orig_string:
        if char.isupper():
            string2 += char.lower()
        elif char.islower():
            string2 += char.upper()
        else:
            string2 += char
    return string2


def split_in_half(orig_string: str):

    n = len(orig_string)
    mitad = int(n/2)
    if n % 2 == 0: # si longitud es par
        string1 = orig_string[0:mitad]
        string2 = orig_string[mitad:]
                              
    else:
        mitad = n // 2
       
        string1 = orig_string[0:mitad]
        string2 = orig_string[mitad:]
                                                            
    return string1, string2

def remove_special_characters(orig_string: str):

    permitido = ascii_letters + digits
    new_string = ""
    
    for char in orig_string:
        if char in permitido or char == " ":
            new_string += char
        else:
            continue    

    return new_string

if __name__ == "__main__":

    my_string = "abcd"

    print(split_in_half(my_string))
