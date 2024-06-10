
def search(products: list, criterion: callable):

    return [product for product in products if criterion(product)]

def price_under_4_euros(product):
    return product[1] < 4



if __name__ == "__main__":

    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]
    print(search(products,price_under_4_euros))