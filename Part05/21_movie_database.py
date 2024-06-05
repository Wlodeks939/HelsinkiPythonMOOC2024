def add_movie(database: list, name: str, director: str, year: int, runtime: int):

    d = {}
    d["name"] = name
    d["director"] = director
    d["year"] = year
    d["runtime"] = runtime
    database.append(d)