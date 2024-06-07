class Series:
    def __init__(self,title,num_seasons,genres:list):
        self.title = title
        self.num_seasons = num_seasons
        self.genres = genres
        self.count = 0
        self.suma = 0
        

    def __str__(self):
        line1 = f"{self.title} ({self.num_seasons} seasons)"
        genre_string = ", ".join(self.genres)
        line2 = f"genres: {genre_string}" 
        line3 = "no ratings"  

        if self.count == 0:
            return f"{line1}\n{line2}\n{line3}"
        else:
            line4 = f"{self.count} ratings, average {(self.suma/self.count):.1f}"
            return f"{line1}\n{line2}\n{line4} points"

    
    def rate(self, rating: int):
    
        if rating >= 0 and rating <= 5:
            self.suma += rating
            self.count += 1

    def get_rating(self):
        return self.suma/self.count        


def minimum_grade(min:int,series_list:list): # devuelve una lista con las series que superan el min de rating
    lista = []

    for serie in series_list:
        if serie.get_rating() > min:
            lista.append(serie)
    return lista

def includes_genre(genre:str,series_list:list): # devuelve una lista con el genero pedido
    lista = []
    for serie in series_list:
        for genre_ in serie.genres:
            if genre == genre_:
                lista.append(serie)
       
    return lista

if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)