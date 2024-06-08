# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        if self._cents < 10:
            return f"{self._euros}.0{self._cents} eur"
        else:
            return f"{self._euros}.{self._cents} eur"
        
    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    def __lt__(self, another):
        if self._euros < another._euros:
            return True
        elif self._euros == another._euros and self._cents < another._cents:
            return True
        else:
            return False
        
    def __gt__(self, another):
        if self._euros > another._euros:
            return True
        elif self._euros == another._euros and self._cents > another._cents:
            return True
        else:
            return False
        
    def __ne__(self, another):
        if self._euros == another._euros and self._cents == another._cents:
            return False
        else:
            return True
        
    def __add__(self, another):
        if self._cents + another._cents >= 100:
            new_euros = self._euros + another._euros + 1
            new_cents = self._cents + another._cents -100
            new_money = Money(new_euros,new_cents)
            return new_money   
        else:
            new_euros = self._euros + another._euros 
            new_cents = self._cents + another._cents 
            new_money = Money(new_euros,new_cents)
            return new_money
        
    def __sub__(self, another):
        if self._euros < another._euros or (self._euros == another._euros and self._cents < another._cents):
            raise ValueError

        else:
            if self._cents < another._cents:
                new_cents = self._cents - another._cents +100
                new_euros = self._euros - another._euros -1
                new_money = Money(new_euros,new_cents)
                return new_money 
            else:
                new_cents = self._cents - another._cents 
                new_euros = self._euros - another._euros
                new_money = Money(new_euros,new_cents)
                return new_money 







