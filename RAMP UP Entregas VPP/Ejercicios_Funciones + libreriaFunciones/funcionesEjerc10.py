def dia (num):
    semana = {"lunes": 1,"martes":2,"miércoles":3,"jueves":4,"viernes":5,"sábado":6,"domingo":7}
    for clave,valor in semana.items():
       if valor == num:
        return clave 
       

def piramide (num):
    lista = []
    for elemento in range(num,0,-1):
        lista.append(elemento)
    lista
    copia = lista.copy()
    for elemento in lista:
        print(str(copia).replace("[","").replace("]", "").replace(","," "))
        copia.pop(0)


def comparativa (a,b):
    if a == b:
        return print (f"Los números {a} y {b} son iguales")
    elif a > b:
        return print(f" El número {a} es mayor que {b}")
    elif a<b:
        return print(f"El número {b} es mayor que {a}")
    

def contador_letra(palabra:str, letra:str):
    contador = 0
    for i in palabra:
        if (i == letra) or (i == letra.upper()) or (i == letra.lower()):
            contador = contador + 1
            
    return contador

def diccionario_palabra (palabra:str):
    diccionario = {}

    for clave, valor in enumerate(palabra):
            diccionario[valor] = clave
    return diccionario

def listarara (lista,comando, elemento = None):
    lista =lista 
    if comando == "add":
        lista.append(elemento)
    elif comando == "remove":
        lista.remove(elemento)
    else:
        print('Escriba el argumento"add" o "remove"')
        return None
    return lista

def frase(*args):
        palabras = " ".join(args)
        return palabras


def serie_fibonacci(n):
    if n <= 0:
        print("Número debe ser mayor que cero")
        return None
    else:
        serie = (n) = (n-1) + (n-2)
        return serie

def a_cuadrado(lado):
    return lado*lado

def a_triangulo (base,altura):
    return (base*altura)/2

def a_circulo(radio):
    import math
    return math.pi*radio**2