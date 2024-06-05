def find_movies(database: list, search_term: str):

    lista = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            lista.append(movie)

    return lista


if __name__ == "__main__":

    database = [{"name": "Gone with the Python 4", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane 2", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers 4", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "4")
    print(my_movies)
