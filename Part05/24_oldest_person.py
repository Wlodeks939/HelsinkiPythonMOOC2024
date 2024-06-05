def oldest_person(people: list):

    oldest = 2024
    for person in people:
        if person[1] < oldest:
            oldest = person[1]
            name_oldest = person[0]
    return name_oldest                             

if __name__ == "__main__":

    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))