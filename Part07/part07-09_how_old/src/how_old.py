from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

nuevo_milenio = datetime(1999, 12, 31)

dif = nuevo_milenio - datetime(year,month,day)

if datetime(year,month,day) >= nuevo_milenio:
    print("You weren't born yet on the eve of the new millennium.")

else:
    print(f"You were {dif.days} days old on the eve of the new millennium.")    