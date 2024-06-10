import json


class App:
    def __init__(self):
        self.lista = []

    def read_file(self):

        filename = input("file name:")

        with open(filename) as my_file:
            data = my_file.read()

        self.lista = json.loads(data) # [{'name': 'Travis Zajac', 'nationality': 'CAN', 'assists': 16, 'goals': 9, 'penalties': 28, 'team': 'NJD', 'games': 69}, 
        print(f"read the data of {len(self.lista)} players")
        print()    

    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")  
        print("4 players in team")
        print("5 players from country")
        print("6 most points")    
        print("7 most goals")   

    def execute(self):
        self.read_file()
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()   
            elif command == "2":
                self.teams()   
            elif command == "3":
                self.countries()    
            elif command == "4":
                self.players_team()   
            elif command == "5":
                self.players_country()   
            elif command == "6":
                self.most_points()     
            elif command == "7":
                self.most_goals()                


    def search_for_player(self):

        name = input("name: ")
        
        for player in self.lista:
            if player["name"] == name:
                team = player["team"]
                goals = player["goals"]
                assists = player["assists"]

        total = goals + assists
        
        print(f"{name:21}{team:3}{goals:4} + {assists:2} = {total:3}")
        
    def teams(self):

        lista_teams = []

        for player in self.lista:
            if player["team"] not in lista_teams:
                lista_teams.append(player["team"])

        for team in sorted(lista_teams):
            print(team)    

    def countries(self):

        lista_countries = []

        for player in self.lista:
            if player["nationality"] not in lista_countries:
                lista_countries.append(player["nationality"])

        for countrie in sorted(lista_countries):
            print(countrie)   


    def players_team(self):

        team = input("team: ")  
        lista2 = [] 

        for player in self.lista:  # arma una nueva lista filtrando por team
            if team == player["team"]:
                player["total"] = player["goals"] + player["assists"]
                lista2.append(player)

        lista3 = sorted(lista2, key=lambda x: x['total'], reverse=True) # ordena por total

        for player in lista3:

            name = player["name"]
            team = player["team"]
            goals = player["goals"]
            assists = player["assists"]
            total = player["total"]

            print(f"{name:21}{team:3}{goals:4} + {assists:2} = {total:3}")


    def players_country(self):

        country = input("country: ")  
        lista2 = [] 

        for player in self.lista:
            if country == player["nationality"]:
                player["total"] = player["goals"] + player["assists"]
                lista2.append(player)

        lista3 = sorted(lista2, key=lambda x: x['total'], reverse=True)

        for player in lista3:

            name = player["name"]
            team = player["team"]
            goals = player["goals"]
            assists = player["assists"]
            total = player["total"]

            print(f"{name:21}{team:3}{goals:4} + {assists:2} = {total:3}")


    def most_points(self):

        lista2 = [] 
        n = int(input("how many: "))

        for player in self.lista:
            player["total"] = player["goals"] + player["assists"]
            lista2.append(player)

        lista3 = sorted(lista2, key=lambda x: (x['total'],x['goals']), reverse=True)

        lista4 = []

        for i in range(n):
            lista4.append(lista3[i])

        for player in lista4:

            name = player["name"]
            team = player["team"]
            goals = player["goals"]
            assists = player["assists"]
            total = player["total"]

            print(f"{name:21}{team:3}{goals:4} + {assists:2} = {total:3}")    


    def most_goals(self):

        lista2 = [] 
        n = int(input("how many: "))

        for player in self.lista:
            player["total"] = player["goals"] + player["assists"]
            lista2.append(player)

        lista3 = sorted(lista2, key=lambda x: (-x['goals'],x['games']))

        lista4 = []

        for i in range(n):
            lista4.append(lista3[i])

        for player in lista4:

            name = player["name"]
            team = player["team"]
            goals = player["goals"]
            assists = player["assists"]
            total = player["total"]

            print(f"{name:21}{team:3}{goals:4} + {assists:2} = {total:3}")              


prueba = App()
prueba.execute()


