matrizA = []
matrizB = []
matrizSuma = []
matrizResta = []
matrizMultipli = []

# Agregando valores a la matriz A
filaA = int(input('Matriz "A" Numero de filas : '))
columnaA = int(input('Matriz "A" Numero de columnas: '))

for i in range (filaA):
    pasaraA = []
    for j in range(columnaA):
        datoA = int(input('numero: '))
        pasaraA.append(datoA)
    matrizA.append(pasaraA)


# Agregando valores a la matriz B

filaB = int(input('Matriz "B" Numero de filas: '))
columnaB = int(input('Matriz "B" Numero de columnas: '))

for i in range (filaB):
    pasaraB = []
    for j in range(columnaB):
        datoB = int(input('numero: '))
        pasaraB.append(datoB)
    matrizB.append(pasaraB)

# suma de las matrices
if filaA == filaB and columnaA == columnaB:
    for i in range(len(matrizA)):
        sumaParcial= []
        for j in range(len(matrizA[0])):
            print(len(matrizA[0]))
            sum = matrizA[i][j] + matrizB[i][j]
            sumaParcial.append(sum)
        matrizSuma.append(sumaParcial)

# Resta de matrices
if filaA == filaB and columnaA == columnaB:
    for i in range(len(matrizA)):
        restaParcial= []
        for j in range(len(matrizA[0])):
            sum = matrizA[i][j] - matrizB[i][j]
            restaParcial.append(sum)
        matrizResta.append(restaParcial)

# Multiplicación de matrices


print('\nMatriz A\n')
print(matrizA)
print('\nMatriz B\n')
print(matrizB)
print('\nLa suma de las matrices\n')
print(matrizSuma)
print('\nLa resta de las matrices\n')
print(matrizResta)
