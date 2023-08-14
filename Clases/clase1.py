def EJE200 ():
    a = input('Ingrese la cadena a: \n')
    b = input('Ingrese la cadena b: \n')
    c = ''
    i = 0
    j = 0

    while(i < len(a)):
        if(a[:i + j]==b[:i+j]):
            c = a[:i + j]
            j += 1
        i += 1

    print("El prefijo comun mas largo entre ambas cadenas es:", c)

def EJE200B ():
    a = input('Ingrese la cadena a: \n')
    b = input('Ingrese la cadena b: \n')
    c = ''
    i = 1

    for character in a:
        if(character in b[:i]):
            c += character
            i += 1
        else:
            break
    
    print("El prefijo comun mas largo entre ambas cadenas es: {0}". format(c))

def EJE201 ():
    a = input('Ingrese la cadena a: \n')
    b = input('Ingrese la cadena b: \n')
    c = input('Ingrese la cadena c: \n')
    d = ''
    i = 0

    for character in a:
        if((character in b[i:i+1]) and (character in c[i:i+1])):
            d += character
            i += 1
        else:
            break
    
    print("El prefijo comun mas largo entre ambas cadenas es: {0}". format(d))

EJE201()

