from random import choice

def word_generator(characters: str, length: int, amount: int):

    lista = []

    for i in range(amount):

        word = ""
        for j in range(length):
            word += choice(characters)

        lista.append(word)  


    return (item for item in lista)

if __name__ == "__main__":

    wordgen = word_generator("abcdefg", 3, 5)
    print(wordgen)
    for word in wordgen:
        print(word)