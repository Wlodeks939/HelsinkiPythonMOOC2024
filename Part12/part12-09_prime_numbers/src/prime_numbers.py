def prime_numbers():

    numero_a_chequear = 2

    while True:
    
        primo = True

        for i in range(2,numero_a_chequear):

            if numero_a_chequear % i == 0:
                primo = False
                break

        if primo:
            yield numero_a_chequear  
            

        numero_a_chequear += 1      



