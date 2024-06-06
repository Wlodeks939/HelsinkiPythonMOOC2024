def store_personal_data(person: tuple):

    with open("people.csv", "a") as my_file:

        line = f"{person[0]};{person[1]};{person[2]}"
        my_file.write(line+"\n")

if __name__ == "__main__":

    store_personal_data(("Paul Paulson", 37, 175.5))   