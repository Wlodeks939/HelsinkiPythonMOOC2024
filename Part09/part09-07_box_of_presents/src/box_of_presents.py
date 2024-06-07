class Present:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"    


class Box:
    def __init__(self):
        self.presents = []
        self.pesototal = 0
    def add_present(self, present: Present):
        self.presents.append(present)  
        self.pesototal += present.weight  
    def total_weight(self):
        return self.pesototal    
    
