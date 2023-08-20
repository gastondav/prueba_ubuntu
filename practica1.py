# Ejercicio 1,2

# imprimir (25)
# imprimir (100)

def imprimir (n):
    if(n%2==0):
        print (n)
    if(n>0):
        return imprimir(n-1) 



def npar (n, m):
    for num in range(m, m+n*2):
        if (num%2==0):
            print (num)

def sumn(n=50):
    if(n>0):
        return n+sumn(n-1)
    return 0

def sumnm(n, m):
    if(n<m):
        return n+sumnm(n+1, m)
    return 0

def duplicar(p, n):
    if(n>0):
        return p+duplicar(p, n-1)
    return ""
# print(duplicar("messi", 8))

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def divi(a,b):
    return a/b

def menu():
    valor=input("Ingrese una opcion \n1. Suma \n2. Resta \n3. Multiplica \n4. Divide\n5. Salir\n")
    if(valor == "1"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return suma(uno,dos)
    if(valor == "2"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return resta(uno,dos)
    if(valor == "3"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return multiplicacion(uno,dos)
    if(valor == "4"):
        uno=int(input("Ingrese un valor: "))
        dos=int(input("Ingrese un segundo valor: "))
        return divi(uno,dos)
    if(valor == "5"):
        return "gil"