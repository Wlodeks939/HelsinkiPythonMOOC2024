# Write your solution here

def most_common_character(text):

    count = 0
    countmax = 0

    for i in range(len(text)):

        count = text.count(text[i])
        if count > countmax:
            countmax = count
            char = text[i]
    return char    



if __name__ == "__main__":

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

    

