# Ejercicio 1,2

# imprimir (25)
# imprimir (100)

def imprimir (n):
    if(n%2==0):
        print (n)
    if(n>0):
        return imprimir(n-1) 

# Ejercicio 3

def npar (n, m):
    for num in range(m, m+n*2):
        if (num%2==0):
            print (num)

# Ejercicio 4 y 5

def sum_n(n=50):
    if(n>0):
        return n + sum_n(n-1)
    return 0

# Ejercicio 6

def sum_n_m(n, m):
    if(n<m):
        return n+sum_n_m(n+1, m)
    return 0

# Ejercicio 7 y 8

def duplicar(p, n):
    if(n>0):
        return p+duplicar(p, n-1)
    return ""
# print(duplicar("messi", 8))

# Ejercicio 9

# a)
def suma(a,b):
    return a+b

# b)
def resta(a,b):
    return a-b

# c)
def multiplicacion(a,b):
    return a*b

# d)
def divi(a,b):
    return a/b

# e)
def menu():
    valor=input("Ingrese una opcion \n1. Suma \n2. Resta \n3. Multiplica \n4. Divide\n5. Salir\n")
    if(valor == "1"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return suma_2(uno,dos)
    if(valor == "2"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return resta_2(uno,dos)
    if(valor == "3"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return multiplicacion_2(uno,dos)
    if(valor == "4"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return divi_2(uno,dos)
    # f)
    if(valor == "5"):
        return "Finaliza el programa"
    
def suma_2(a,b):
    print (a+b)
    return menu()

def resta_2(a,b):
    print (a-b)
    return menu()

def multiplicacion_2(a,b):
    print (a*b)
    return menu()

def divi_2(a,b):
    print (a/b)
    return menu()