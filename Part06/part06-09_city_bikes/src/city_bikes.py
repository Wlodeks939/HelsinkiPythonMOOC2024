import math

def get_station_data(filename: str):

    with open(filename) as file:
        content = file.read()

    # creacion lista de strings. Cada string es una estacion
    # en metodo split, usamos "\n" para usar los saltos de linea como separador. Si usamos split()
    # va a separar tambien cuando llegue a "Vanha kirkkopuisto". De esta manera ignora ese espacio
           
    lista_str = content.split("\n")  #  ['24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001',
    lista_str.pop(0) # elimina encabezado

    
    # creamos lista de listas. Cada lista es una estacion
    lista_estaciones = [] # [['24.950292890004903', '60.155444793742276', '1', 'Kaivopuisto', '30', 'Yes', '001'], 

    for string in lista_str:
        if string != "" and string != " ": # esto es para evitar agregar lineas vacias
                                           # si agregas una linea vacia dsp cuando queres convertir a float
                                           # va a tirar error  
            lista = string.split(";")
            lista_estaciones.append(lista)

    # transformamos las coordenadas a float
    for lista in lista_estaciones:  
        temp = lista[0]
        lista[0] = float(temp) 
        temp2 = lista[1]
        lista[1] = float(temp2) 

    # creamos diccionario. key va el nombre y value una tupla con las coordenadas
    dict_estaciones = {}
    for lista in lista_estaciones:
        dict_estaciones[lista[3]] = (lista[0],lista[1])

    return dict_estaciones  # {'Kaivopuisto': (24.950292890004903, 60.15544479374228),


def distance(stations: dict, station1: str, station2: str):

    longitude1 = stations[station1][0] # accedes al diccionario con la llave name station1 y asignas el
                                       # primer valor de la tupla [0] 
    longitude2 = stations[station2][0]

    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1] # accedes al diccionario con la llave name station2 y asignas el
                                        # segundo valor de la tupla [1] que es la latidud

    # formulas dadas en enunciado
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict):

    max_dist = 0
    
    # creamos una lista con los nombres de las estaciones
    lista_estaciones = []
    for key in stations:
        lista_estaciones.append(key)

    for estacion in lista_estaciones:
        for estacion2 in lista_estaciones:
            if estacion != estacion2:
                temp = distance(stations, estacion, estacion2)
                if temp > max_dist:
                    max_dist = float(temp)
                    lista_2_estaciones = [] # aca vamos a agregar las 2 estaciones con mayor distancia
                    lista_2_estaciones.append(estacion)
                    lista_2_estaciones.append(estacion2)


    return lista_2_estaciones[0], lista_2_estaciones[1], max_dist      


if __name__ == "__main__":

    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

    