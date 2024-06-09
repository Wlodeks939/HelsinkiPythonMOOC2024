
def balanced_brackets(my_string: str):

    newstr = ""
    for char in my_string:  # para sacar los caracteres que no son ()[]
        if char in "[]()":
            newstr += char


    if len(newstr) == 0:
        return True
    if not (newstr[0] == '(' and newstr[-1] == ')') and not (newstr[0] == '[' and newstr[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(newstr[1:-1])

