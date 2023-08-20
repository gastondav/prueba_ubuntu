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
      m = int(input("Ingrese un valor: "))
      for i in range (1, m + 1):
            valor = factorial_aux(i)
            print(valor)
