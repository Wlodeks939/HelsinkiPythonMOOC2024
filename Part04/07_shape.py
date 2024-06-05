# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(n,text):
    if text == "":
        print("*" * n)
    else:
        print(text[0] * n)

def triangle(size,text):
    # You should call function line here with proper parameters
    n = size
    k = size - 1
    while n > 0:
        line(size-k, text)
        n -= 1
        k -= 1       

def rectangle(ancho,alto,text):

    n = alto
    while n > 0:
        line(ancho,text)
        n -= 1



def shape(size1, text1, size2, text2):
    triangle(size1,text1)
    rectangle(size1,size2,text2)


if __name__ == "__main__":
    
    shape(5, "x", 2, "o")