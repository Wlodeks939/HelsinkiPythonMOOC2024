def order_by_seasons(item: dict):
    return item["seasons"]



def sort_by_seasons(items: list):

    return sorted(items, key=order_by_seasons)

