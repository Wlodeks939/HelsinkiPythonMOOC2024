class Recording:
    def __init__(self,length):
        if length < 0:
            raise ValueError
        else:
            self.__length = length

    def __str__(self):
        return self.__length

    @property
    def length(self):
        return self.__length

    @length.setter 
    def length(self,length):
        if length < 0:
            raise ValueError
        elif length > 0:
            self.__length = length


