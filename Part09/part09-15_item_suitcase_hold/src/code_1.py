class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"    

 
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight


class Suitcase:
    def __init__(self,max):
        self.max = max
        self.suit = []
        self.pesoactual = 0

    def add_item(self,item:Item):
        if item.weight() + self.pesoactual <= self.max:
            self.suit.append(item)
            self.pesoactual += item.weight()

    def print_items(self):

        for item in self.suit:
            print(item)  

    def weight(self):
        return self.pesoactual      

    def heaviest_item(self):

        if len(self.suit) == 0:
            return None
        else:
            mayor_peso = 0
            for item in self.suit:
                if item.weight() > mayor_peso:
                    mayor_peso = item.weight()
                    mayor_item = item  

        return mayor_item

    def __str__(self):
        if len(self.suit) == 1:
            return f"{len(self.suit)} item ({self.pesoactual} kg)"    
        else:
            return f"{len(self.suit)} items ({self.pesoactual} kg)"      


class CargoHold:
    def __init__(self,max):
        self.max = max
        self.cargo = []
        self.pesoactual = 0

    def add_suitcase(self,suit:Suitcase):

        if suit.weight() + self.pesoactual <= self.max:
            self.cargo.append(suit)
            self.pesoactual += suit.weight()

    def print_items(self):
        for suitcase in self.cargo:
            suitcase.print_items()   


    def __str__(self):
        if len(self.cargo) == 1:
            return f"{len(self.cargo)} suitcase, space for {self.max - self.pesoactual} kg"    
        else:
            return f"{len(self.cargo)} suitcases, space for {self.max - self.pesoactual} kg" 



if __name__ == "__main__":
    
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)


    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)


    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()