def order_by_stock(item: tuple):
    return item[2]



def sort_by_remaining_stock(items: list):

    return sorted(items, key=order_by_stock)


