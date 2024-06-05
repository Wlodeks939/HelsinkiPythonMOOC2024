# Write your solution here
# You can test your function by calling it within the following block

def greatest_number(a,b,c):

    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    elif a==b or a==c:
        return a
    else:
        return c


if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)