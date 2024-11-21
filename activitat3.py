#Totes les respostes han d’estar amb f-string.

Imprimir números de l’1 al 10 (amb for i amb while)

#While
x = 1
while x <= 10:
    print(f"Número actual (while): {x}")
    x += 1

# for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(f"Número actual (for): {i}")

Sumar els primers 10 números utilitzant for i range().

# Inicialitzem la suma a 0
suma = 0
for num in range(10):
    suma += num

# Iterem pels números de 0 a 9 (10 no inclòs)
for num in range(10):
    suma += num  # Afegim cada número a la suma

Imprimir els elements d'una llista amb for. fruits = [“poma”,”pera”,”raïm”,”plàtan”]

# El que volem imprimir

fruits = ["poma", "pera", "raïm", "plàtan"]
for fruit in fruits:
    print(f"Fruit: {fruit}")


#Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
for n in num:
    if n % 2 == 0:
        print(f"Número parell: {n}")
    else:
        print(f"Número imparell: {n}")


#Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.

num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
suma_parells = 0
suma_imparells = 0
for n in num:
    if n % 2 == 0:
        suma_parells += n
    else:
        suma_imparells += n
print(f"Suma de números parells: {suma_parells}")
print(f"Suma de números imparells: {suma_imparells}")

#Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.

suma = 0
x = 0
while suma < 100:
    suma += x
    print(f"Número afegit: {x}, Suma acumulada: {suma}")
    x += 1
print(f"La suma ha arribat a 100 o més: {suma}")

#Amb while indicar si el número guardat a una variable està entre 100 i 400.

num = 250  # Posem un valor
verificant = True

while verificant:
    if 100 <= num <= 400:
        print(f"El número {num} està entre 100 i 400.")
    else:
        print(f"El número {num} no està entre 100 i 400.")
    verificant = False  # Finalitzem el programa
