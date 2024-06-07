# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        self.numbers += number
        self.count += 1


    def count_numbers(self):
        return self.count

    def get_sum(self):
        if self.count == 0:
            return 0
        else:
            return self.numbers
        
    def average(self):
        if self.count == 0:
            return 0
        else:
            return self.numbers/self.count



objeto_suma_total = NumberStats()
objeto_suma_even = NumberStats()
objeto_suma_odd = NumberStats()
print("Please type in integer numbers:")
while True:
    num = int(input(""))
    if num == -1:
        break

    objeto_suma_total.add_number(num)    

    if num % 2 == 0:
        objeto_suma_even.add_number(num)
    if num % 2 != 0:
        objeto_suma_odd.add_number(num)    

print(f"Sum of numbers: {objeto_suma_total.get_sum()}")
print(f"Mean of numbers: {objeto_suma_total.average():.2f}")
print(f"Sum of even numbers: {objeto_suma_even.get_sum()}")
print(f"Sum of odd numbers: {objeto_suma_odd.get_sum()}")
    
