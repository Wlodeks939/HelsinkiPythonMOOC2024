# Write your solution here



def list_sum(a,b):

    lista = []

    n = int(len(a)) 

    for _ in range(n):
        lista.append(int(a[_]) + int(b[_]))

    return lista  


if __name__ == "__main__":

    main()
   