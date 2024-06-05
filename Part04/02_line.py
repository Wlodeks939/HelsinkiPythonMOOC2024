# Write your solution here
# You can test your function by calling it within the following block

def line(n,text):
    if text == "":
        print("*" * n)
    else:
        print(text[0] * n)


if __name__ == "__main__":
    line(10, "LOL")