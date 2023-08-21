# Ejercicio 1
def imprimir_10_20():
    for i in range (10,21):
            print (i)

# Ejercicio 2
def domino():
      for i in range(1,29):
            print(i)

# Ejercicio 3

def juego(n):
      for i in range(1,n+1):
            print(i)

# Ejercicio 4

def factorial_aux(n):
      factorial = 1
      for i in range (1,n+1):
            factorial = factorial * i
      return (factorial)

def fact_m():
      m = int(input("Ingrese la cantidad de numeros: "))
      for i in range (1, m + 1):
            n = int (input ("Ingrese un numero: "))
            valor = factorial_aux(n)
            print(str(n) + "! = " + str(valor))

# Ejercicio 5

def farCel (f) :
    return (f -32) *5/9

def tabla():
      for i in range (0,121,10):
            print (farCel (i))

# Ejercicio 6

def suma_n(n):
      suma = 0
      for i in range(0,n+1):
            suma = suma + i
      return suma

def triang(m):
      for i in range (1, m+1):
            valor = suma_n(i)
            print(str(i) + " - " + str(valor))
            
# Ejercicio 7

def pos():
      n = int (input ("Ingrese un numero positivo: "))    
      while not (n > 0):
            n = int (input ("Error, volver a ingresar un numero positivo: "))

# Ejercicio 8

def ingresar():
      l=[]
      contador = 0
      print("Ingresar Notas: ")
      valor = True
      nota = int (input ("Ingrese una nota: "))
      l[0:0]= {nota}
      while valor:
        valor = input ("Quiere ingresar una nota: ")
        if valor == "no":
              valor = False
        else: 
              nota = int (input ("Ingrese una nota: "))
              l[0:0]= {nota}
              contador = contador + 1
      print (prom (l,contador))

def prom(l,contador):   # calcula el promedio, recibe la lista y el largo de la misma
      suma = 0
      for i in range (0, contador+1):
            suma = suma + l[i]
      print("El promedio es: " + str (suma))

# Ejercicio 9

