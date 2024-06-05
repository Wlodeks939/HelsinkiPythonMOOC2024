# Write your solution here

lista = []
i = 0
salir = True

while salir:

    word = input("Word:")

   
    if word in lista:
        print(f"You typed in {i} different words")
        salir = False
    else:
        lista.append(word)
        i += 1

    
  
        