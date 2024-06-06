entrada = input("Write text:")
#entrada = "This is acually a good and usefull program"

with open("wordlist.txt") as file:
        content = file.read()

lista_str = content.split() # lista de strings que son palabras

lista_entrada = entrada.lower().split()  # ['we', 'use', 'ptython', 'to', 'make', 'a', 'spell', 'checker']

nuevo_string = ""
lista_errores = []

# crea una lista de errores con las palabras que no encuentra en el diccionario
for word in lista_entrada:
        if word not in lista_str:
                lista_errores.append(word)


# itera sobre todos los errores. Por cada error lo busca en el string y lo reemplaza por *error*             
for error in lista_errores:
        entrada = entrada.replace(error,f"*{error}*")


print(entrada)        
