class BankAccount:
    def __init__(self, name, acc_num, balance):
        self.__name = name
        self.__acc_num = acc_num
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        if amount <= self.__balance*1.01:
            self.__balance -= amount   
            self.__service_charge() 

    @property
    def balance(self):
        return self.__balance
    
    def __service_charge(self):
        self.__balance = self.__balance * 0.99




