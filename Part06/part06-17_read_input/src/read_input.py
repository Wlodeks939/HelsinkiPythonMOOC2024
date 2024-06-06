def read_input(texto, a, b):

    while True:

        try:

            entrada = int(input(texto))
            if entrada > a and entrada < b:
                return entrada
        except ValueError:
            pass   
        print(f"You must type in an integer between {a} and {b}")        

if __name__ == "__main__":

    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)        






