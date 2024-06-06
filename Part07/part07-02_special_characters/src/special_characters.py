from string import *

def separate_characters(my_string: str):

    string_ascii = ""
    string_pun = ""
    string_other = ""

    for str in my_string:
        if str in ascii_letters:
            string_ascii += str
        elif str in punctuation:
            string_pun += str
        else:
            string_other += str   

    return string_ascii, string_pun, string_other             



