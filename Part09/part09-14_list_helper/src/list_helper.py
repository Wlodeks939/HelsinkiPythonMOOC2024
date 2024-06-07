class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        dic = {}

        for item in my_list:
            if item not in dic:
                dic[item] = 1
            elif item in dic:
                dic[item] += 1

       
     
        cant_mayor_frec = 0
        for key,value in dic.items():
            if value > cant_mayor_frec:
                num_mayor_frec = key
                cant_mayor_frec = value

        return num_mayor_frec  

    @classmethod
    def doubles(cls,my_list: list): 
        dic = {}

        for item in my_list:
            if item not in dic:
                dic[item] = 1
            elif item in dic:
                dic[item] += 1

        count = 0
        for key,value in dic.items(): 
            if value >= 2:  
                count += 1

        return count        

