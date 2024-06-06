from random import choice

def roll(die: str):

    dado_A = [3,3,3,3,3,6]
    dado_B = [2,2,2,5,5,5]
    dado_C = [1,4,4,4,4,4]

    if die == "A":
        salida = choice(dado_A)
    elif die == "B":
        salida = choice(dado_B)
    elif die == "C":
        salida = choice(dado_C)           

    return salida



def play(die1: str, die2: str, times: int):

    cont1 = 0
    cont2 = 0
    cont_empate = 0

    for i in range(times):

        res_dado1 = roll(die1)
        res_dado2 = roll(die2)

        if res_dado1 > res_dado2:
            cont1 += 1 
        elif res_dado2 > res_dado1:
            cont2 += 1    
        else:
            cont_empate += 1

    return cont1, cont2, cont_empate             


if __name__ == "__main__":

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)