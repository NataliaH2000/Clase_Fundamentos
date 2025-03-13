# Definir una matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 5, 6],
    [3, 8, 1]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Valor {valor} encontrado en la posición ({i}, {j})")
                return
    print(f"Valor {valor} no encontrado en la matriz.")

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Imprimir la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar una fila específica (por ejemplo, la fila 1)
fila_ordenar = 1
ordenar_fila(matriz, fila_ordenar)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)

# Buscar un valor específico
valor_buscar = 5
buscar_valor(matriz, valor_buscar)