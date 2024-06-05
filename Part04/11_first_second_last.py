# Write your solution here
# You can test your function by calling it within the following block

def first_word(text):

    z = text.find(" ")
    return text[0:z]

def second_word(text):

    return text.split()[1]

def last_word(text):

    return text.split()[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word("it was a dark and stormy python"))
    print(second_word("it was a dark and stormy python"))
    print(last_word(sentence))