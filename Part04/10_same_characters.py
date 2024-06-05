# Write your solution here
# You can test your function by calling it within the following block

def same_chars(text,a,b):
    a = int(a)
    b = int(b)

    if a >= len(text) or b >= len(text):
        return False
    if text[a] == text[b]:
        return True
    elif text[a] != text[b]:
        return False


if __name__ == "__main__":
    print(same_chars("abc", 0, 3))