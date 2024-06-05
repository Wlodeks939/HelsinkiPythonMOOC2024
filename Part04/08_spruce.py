# Write your solution here
# You can test your function by calling it within the following block

def spruce(n):
    print("a spruce!")
    i = 1
    while i <= n:

        k = n - i
        stars = 2 * i - 1
        print(" " * k + "*" * stars)
        i += 1
    print(" " * (n - 1) + "*")

if __name__ == "__main__":
    spruce(5)