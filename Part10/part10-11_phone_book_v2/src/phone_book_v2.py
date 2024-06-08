
# Write your solution here:
class Person:
    def __init__(self,name:str):
        self.name_person = name
        self.numbers_person = []
        self.address_person = None

    def add_number(self,number:str):
        self.numbers_person.append(number) 

    def add_address(self,address:str):
         self.address_person = address

    def name(self):
        return self.name_person
    
    def numbers(self):
        return self.numbers_person
    
    def address(self):
        return self.address_person

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            person = Person(name)
            self.__persons[name] = person
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):  
        if not name in self.__persons:
            person = Person(name)
            self.__persons[name] = person
        self.__persons[name].add_address(address)  

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)    

    def search(self):
        name = input("name: ")
        
        if self.__phonebook.get_entry(name) == None: # no direccion, no numero
            print("address unknown") 
            print("number unknown")
            return
        
        person = self.__phonebook.get_entry(name) #  objeto person 

        if person.address() == None and len(person.numbers()) != 0: # no direccion, si numero
            print("address unknown") 
            numbers = person.numbers()                # numbers es una lista de numeros 
            for number in numbers:
                print(number)


        elif person.address() != None and len(person.numbers()) == 0:  # si direccion, no numero
            print("number unknown")    
            print(person.address())                  
        
        else:   # si direccion si numero                                                  
            numbers = person.numbers()                # numbers es una lista de numeros 
            for number in numbers:
                print(number) 
            print(person.address())          

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()    
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

