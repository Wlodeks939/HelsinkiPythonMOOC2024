from datetime import datetime

def is_it_valid(pic: str):

    if len(pic) != 11:
        return False
    
    try:
    
        dd = int(pic[0:2])
        mm = int(pic[2:4])
        yy = int(pic[4:6])

        century = pic[6]

        yyy = int(pic[7:10])

        z = pic[10]

        control_character = pic[0:6] + pic[7:10]
        control_character_index = int(control_character) % 31

        string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

        control_character2 = string[control_character_index]

        if z != control_character2:
            return False

        if dd < 1 or dd > 31 or mm < 1 or mm > 12 or yy < 0 or yy > 99 or century not in ["+","-","A"]:
            return False
        
        if not str(yyy).isdigit():
            return False
        

        if century == '-':
            century2 = 1800
        elif century == '+':
            century2 = 1900
        elif century == 'A':
            century2 = 2000
        
        dob_year = century2 + yy

        datetime(dob_year, mm, dd)
        
        return True
    
    except:
        return False


if __name__ == "__main__":
    print(is_it_valid("290200-1239"))