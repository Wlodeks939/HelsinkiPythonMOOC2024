# Copy here code of line function from previous exercise

def line(n,text):
    if text == "":
        print("*" * n)
    else:
        print(text[0] * n)


def box_of_hashes(height):
    # You should call function line here with proper parameters
    n = height
    while n > 0:
        line(10, "#")
        n -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
