class SimpleDate:
    def __init__(self,day:int,month:int,year:int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"    

    def __eq__(self, another):
        if self.day == another.day and self.month == another.month and self.year == another.year:
            return True
        else:
            return False
        
    def __ne__(self, another):  
        if self.day == another.day and self.month == another.month and self.year == another.year:
            return False
        else:
            return True

    def __lt__(self, another):

        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day < another.day:
            return True
        else:
            return False      
        
    def __gt__(self, another):   

        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day > another.day:
            return True
        else:
            return False 
        
    def __add__(self, n:int):

        newdate = SimpleDate(self.day,self.month,self.year) 
        days = n

        anio = days // 360 # ej 400 // 360 = 1
        dias_restantes = days % 360  # ej 400 % 360 = 40
        meses = 0 # se asigna 0 porque si el if no se ejecuta no tomaria ningun valor esta variable

        if dias_restantes > 30:
            meses = dias_restantes // 30  # 40 // 30 = 1
            dias_restantes = dias_restantes % 30  # 40 % 30 = 10

        # ej 400 dias lo transformo a 1 anio, 1 mes y 10 dias con las variables anio,meses y dias_restantes    
        # ej 28.12.1985 + 10 dias, 1 mes, 1 anio = 38.13.1986


        new_day = newdate.day + dias_restantes #38
        new_month = newdate.month + meses      #13
        new_year = newdate.year + anio         #1986

        if new_day > 30:  #38 > 30
            new_day = new_day - 30  # 8
            new_month += 1          # 14
        if new_month > 12:  # 14 > 12
            new_month = new_month - 12   # 2
            new_year += 1                # 1987

        newdate = SimpleDate(new_day,new_month,new_year)  #8.2.1987

        return newdate   
    
    def __sub__(self, another):

     
        dias_self = self.day + (self.month - 1)*30 + (self.year - 1)*360
        dias_another = another.day + (another.month - 1)*30 + (another.year - 1)*360
        return abs(dias_self - dias_another)


