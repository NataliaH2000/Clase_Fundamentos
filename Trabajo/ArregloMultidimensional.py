#define una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i,j # retorna
    return None
# valor a buscar
numero_buscar=3

#llamo a la funcion
resultado= buscar_valor(matriz, numero_buscar)
if resultado:
    print(f"el resultado del numero {numero_buscar} se encuentra en la posisicion {resultado[1]} ")
else:
    print(f"el resultado no se encontro")