# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to):
        if self.square_metres > compared_to.square_metres:
            return True
        else:
            return False
        

    def price_difference(self, compared_to):
        priceself = self.square_metres * self.price_per_sqm
        price2 = compared_to.square_metres * compared_to.price_per_sqm

        if priceself > price2:
            return priceself - price2
        else:
            return price2 - priceself


    def more_expensive(self, compared_to):
        priceself = self.square_metres * self.price_per_sqm
        price2 = compared_to.square_metres * compared_to.price_per_sqm

        if priceself > price2:
            return True
        else:
            return False
