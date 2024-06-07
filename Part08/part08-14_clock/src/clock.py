class Clock:
    def __init__(self,hours,minutes,seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"   
    def tick(self):
        self.seconds += 1
        if  self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.seconds = 0
            self.minutes = 0 
            self.hours += 1
        if self.hours == 24:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
    def set(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0


             