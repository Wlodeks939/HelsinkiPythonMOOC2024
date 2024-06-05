
def palindromes(text):
    k = len(text) - 1
    count = 0
    for i in range(int(len(text)/2)):

        if text[i] != text[k]:
            count += 1
        k -= 1

    if count == 0:
        return True
    else:
        return False        


def main():
    while True:
        text = input("Please type in a palindrome:")
        if palindromes(text):
            print(f"{text} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")


main()
   

if __name__ == "__main__":

    main()
   

