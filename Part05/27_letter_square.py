layers = int(input("Layers:"))

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L",
            "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

L = layers * 2 - 1
matriz = []

# creacion matriz vacia LxL
for i in range(L):
    fila = [None] * L
    matriz.append(fila)

for k in range(layers):
    for i in range(k,L-k):
        for j in range(k,L-k):
            matriz[i][j] = alphabet[layers-k-1]

# print 
for i in range(L):
    for j in range(L):
        print(matriz[i][j],end="") 
    print()    


"""

explicacion: Primero se genera un cuadrado de LxL de "D"
             Luego un cuadrado de(L-2)x(L-2) de "C" adentro del cuadrado de "D"
             Luego un cuadrado de(L-4)x(L-4) de "B" adetro del cuadrado de "C" ..

 for i in range(0,L-0):
    for j in range(0,L-0):
        matriz[i][j] = "D"

for i in range(1,L-1):
    for j in range(1,L-1):
        matriz[i][j] = "C"   

for i in range(2,L-2):
    for j in range(2,L-2):
        matriz[i][j] = "B"  

Entonces hay que generar Layers cuadrados con un tercer bucle for:

for k in range(layers):
    for i in range(k,L-k):
        for j in range(k,L-k):
            matriz[i][j] = alphabet[layers-k-1]


"""

