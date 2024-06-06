from datetime import *

file_name = input("Filename:")
starting_date = input("Starting date:") # 24.6.2020
starting_date2 = datetime.strptime(starting_date, "%d.%m.%Y")  # 2020-06-24 00:00:00
starting_date3 = starting_date2.strftime("%d.%m.%Y")  # 24.06.2020
ndays = int(input("How many days:"))

lista_str = []  


# popula lista con los tiempos. lista_str es una lista de strings: ['10 20 30', '45 25 60']
for i in range(ndays):
    temp_date = (starting_date2 + timedelta(days=i)).strftime("%d.%m.%Y")
    temp = input(f"Screen time {temp_date}:")
    lista_str.append(temp)


# total minutes

lista_int = []  # [60, 150]

for str in lista_str:
    a,b,c = str.split(" ")
    total_dia = int(a) + int(b) + int(c)
    lista_int.append(total_dia)

total_min = 0

# average minutes

for num in lista_int:
    total_min += num

avg_min = total_min / ndays


# lista strings 2

lista_str2 = []  # ['24.06.2020: 10/20/30', '25.06.2020: 40/50/60']

k = 0

for str in lista_str:
    a,b,c = str.split(" ")
    temp_date = (starting_date2 + timedelta(days=k)).strftime("%d.%m.%Y")
    temp = f"{temp_date}: {a}/{b}/{c}"
    lista_str2.append(temp)
    k +=1


with open(file_name, "w") as my_file:    

    line = f"Time period: {starting_date3}-{(starting_date2 + timedelta(days=ndays-1)).strftime("%d.%m.%Y")}"
    my_file.write(line+"\n")
    line = f"Total minutes: {total_min}"
    my_file.write(line+"\n")
    line = f"Average minutes: {avg_min:.1f}"
    my_file.write(line+"\n")

    for str in lista_str2:
        my_file.write(str+"\n")

   
