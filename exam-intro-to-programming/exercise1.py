num_list = []

while True:
    
    num = int(input("Type in a number: "))   
    if num == 0:
        break 

    num_list.append(num)

    
sum = 0
for num in num_list:
    sum += num

dic = {}
for num in num_list:    
    if num not in dic:
        dic[num] = 0
    elif num in dic:
        dic[num] += 1    

num_max = 0
most_repeated = 0
for key,value in dic.items():
    if value > num_max:
        num_max = value
        most_repeated = key


print(f"Biggest: {max(num_list)}")
print(f"Smallest: {min(num_list)}")
print(f"Number of numbers: {len(num_list)}")
print(f"Sum: {sum}")
print(f"Most repeated: {most_repeated}")