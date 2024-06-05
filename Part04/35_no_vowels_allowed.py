# Write your solution here

def no_vowels(text):

    vocales = ['a','e','i','o','u']
    new_text = ""

    for char in text:
        if char in vocales:
            new_text += ""
        else:
            new_text += char   

    return new_text      



if __name__ == "__main__":

    print(no_vowels("twitter"))