# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.alturatotal = 0
    
    def add(self, person: Person):
        self.persons.append(person) 
        self.alturatotal += person.height

    def is_empty(self):
        if len(self.persons) == 0:
            return True
        else:
            return False
    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.alturatotal} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):

        
        if len(self.persons) == 0:
            return None
        else:
            enano = self.persons[0]
            altura_enano = self.persons[0].height
            for person in self.persons:
                if person.height < altura_enano:
                    enano = person
                    altura_enano = person.height
            return enano      

    def remove_shortest(self):

        if len(self.persons) == 0:
            return None
        else:
            altura_enano = self.persons[0].height
            j = 0 # contador
            k = 0 # registra el indice del enano
            for person in self.persons:
                if person.height < altura_enano:
                    altura_enano = person.height
                    k = j
                j += 1

            self.alturatotal -= self.persons[k].height      
            return self.persons.pop(k)
        




