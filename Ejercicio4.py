matrizA = []
matrizTranspuesta = []

# Agregando valores a la matriz A
filaA = int(input('Matriz "A" Numero de filas : '))
columnaA = int(input('Matriz "A" Numero de columnas: '))

for i in range (filaA):
    pasaraA = []
    for j in range(columnaA):
        datoA = int(input('numero: '))
        pasaraA.append(datoA)
    matrizA.append(pasaraA)

# Hallamos la transpuesta de la matriz

for i in range(len(matrizA[0])):
    matrizAuxil = []
    for j in range (len(matrizA)):
        matrizAuxil.append(matrizA[j][i])
    matrizTranspuesta.append(matrizAuxil)

# imprimimos la matriz

print('La matriz: \n')
for linea in matrizA:
    for elemento in linea:
        print(elemento, end =' ')
    print()

print('\nLa matriz transpuesta: \n')

#Imprimimos la matriz transpuesta
for linea in matrizTranspuesta:
    for elemento in linea:
        print(elemento, end =' ')
    print()
