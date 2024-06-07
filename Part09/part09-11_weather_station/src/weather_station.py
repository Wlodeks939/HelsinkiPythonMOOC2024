class WeatherStation:
    def __init__(self,name):
        self.__name = name
        self.__obs = []

    def add_observation(self, observation: str):
        self.__obs.append(observation)

    def latest_observation(self):
        if len(self.__obs) > 0:
            return self.__obs[-1]  
        elif len(self.__obs) == 0:
            return ""
        
    def number_of_observations(self):
        return len(self.__obs)  

    def __str__(self):
        return f"{self.__name}, {len(self.__obs)} observations"   



