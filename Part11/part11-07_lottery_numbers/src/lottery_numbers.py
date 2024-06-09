class LotteryNumbers:
    def __init__(self,week:int,lista:list):
        self.week = week
        self.lista = lista

    def number_of_hits(self,numbers: list):
        return len([item for item in numbers if item in self.lista])


    def hits_in_place(self,numbers):
        return [item if item in self.lista else -1 for item in numbers]
    


