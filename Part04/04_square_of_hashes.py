# Copy here code of line function from previous exercise

def line(n,text):
    if text == "":
        print("*" * n)
    else:
        print(text[0] * n)


def square_of_hashes(size):
    # You should call function line here with proper parameters
    n = size
    while n > 0:
        line(size, "#")
        n -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
