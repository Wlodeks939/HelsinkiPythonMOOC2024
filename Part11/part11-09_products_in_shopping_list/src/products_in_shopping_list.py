# WRITE YOUR SOLUTION HERE:
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration
        

def products_in_shopping_list(shopping_list, amount: int):
    return [item[0] for item in shopping_list if item[1] >= amount]     

     # item es una tupla de dos elementos       
     # item[0] primer elemento de la tupla:nombre / item[1]: number 