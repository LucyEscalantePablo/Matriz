matrizA = []
diagonalMatriz = []

# Agregando valores a la matriz A

filaA = int(input('Matriz "A" Numero de filas : '))
columnaA = int(input('Matriz "A" Numero de columnas: '))

for i in range (filaA):
    pasaraA = []
    for j in range(columnaA):
        datoA = int(input('numero: '))
        pasaraA.append(datoA)
    matrizA.append(pasaraA)

# Hallamos la diagonal de la matriz

if filaA == columnaA:
    for i in range (len(matrizA)):
        for j in range (len(matrizA[0])):
            if i==j:
                diagonalMatriz.append(matrizA[i][j])
    
# Mostramos la matriz

print('La matriz: \n')
for linea in matrizA:
    for elemento in linea:
        print(elemento, end =' ')
    print()

print('\nLa diagonal de la matriz es: \n')
print(diagonalMatriz)
