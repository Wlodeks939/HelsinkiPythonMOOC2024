# Write your solution here

while True:
    string = input("Editor: ")
    
    if "visual studio code" == string.lower():
        print("an excellent choice!")
        break
    if "word" == string.lower():
        print("awful")
    else:
        print("not good")
