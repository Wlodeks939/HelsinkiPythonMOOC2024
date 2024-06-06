name = input("Whom should I sign this to:")
name_file = input("Where shall I save it:")

with open(name_file, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
