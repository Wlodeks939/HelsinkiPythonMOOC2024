# Copy here code of line function from previous exercise

def line(n,text):
    if text == "":
        print("*" * n)
    else:
        print(text[0] * n)


def triangle(size):
    # You should call function line here with proper parameters
    n = size
    k = size - 1
    while n > 0:
        line(size-k, "#")
        n -= 1
        k -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
