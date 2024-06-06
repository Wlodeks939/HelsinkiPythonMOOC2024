def find_words(search_term: str):

    with open("words.txt") as file:
        content = file.read()

        lista_str = content.split("\n") # , ['zymoscope', 'zymurgy', 'zyzzyva', 'zyzzyvas'..

    lista_match = []

    # caso general

    for str in lista_str:
        if search_term == str:
            lista_match.append(str)


    # Asterisk * at the end: Any word which begins with the search term is acceptable
            # For example, ca* would yield words like california, cat
            
    for str in lista_str:
        if search_term.endswith("*") and str.startswith(search_term[:-1]):
            lista_match.append(str)


    # Asterisk * at the beginning: Any word which ends with the search term is acceptable
            
    for str in lista_str:
        if search_term.startswith("*") and str.endswith(search_term[1:]):
            lista_match.append(str)        



    # Dot: A dot . means that any single character is acceptable in its place. 
            # ca. would yield words like cat and car, p.ng would yield words like ping and pong

    for str in lista_str:
        if "." in search_term and len(str) == len(search_term):
            temp = True
            for j in range(len(search_term)):
                if search_term[j] == ".": 
                    continue            # ignora el ".". Continua con el bucle
                if search_term[j] != str[j]:
                    temp = False        # sin un caracter ya no es igual, no se graba la palabra
            if temp:
                lista_match.append(str)


    
    #print(lista_match)
   
    return lista_match

#find_words("reson*")