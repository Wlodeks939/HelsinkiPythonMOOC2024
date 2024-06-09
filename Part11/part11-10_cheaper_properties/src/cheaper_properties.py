class RealProperty:
    def __init__(self, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        # Function abs returns absolute value
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0


    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')

def cheaper_properties(properties: list, reference: RealProperty):

    return [(casa,casa.price_difference(reference)) for casa in properties if reference.more_expensive(casa)]


if __name__ == "__main__":
    a1 = RealProperty(1, 50, 1000, "casa1")
    a2 = RealProperty(1, 50, 3000, "casa2")
    a3 = RealProperty(1, 50, 2500, "casa3")
    a4 = RealProperty(1, 50, 500, "casa4")
    a5 = RealProperty(1, 50, 5000, "casa5")


    properties = [a1, a2, a3, a4, a5]

    print(cheaper_properties(properties, a3))

