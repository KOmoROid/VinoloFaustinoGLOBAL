seguir = 'S'

while seguir == 'S':
    def isMutant(lista):

    #Recorrido de filas, columnas y diagonales
    #Para las filas

        for fila in lista:
            if seRepite(fila):
                return True
        
    #Para las columnas

        for j in range(len(lista[0])):
            columna = [fila[j] for fila in lista]
            if seRepite(columna):
                return True
            
    #Para las diagonales
    #Principal

        for i in range(len(lista) - 3):
            for j in range(len(lista[0]) - 3):
                diagonal_principal = [lista[i + k][j + k] for k in range(4)]
                if seRepite(diagonal_principal):
                    return True
                
    #Inversa
    
        for i in range(3, len(lista)):
            for j in range(len(lista[0]) - 3):
                diagonal_secundaria = [lista[i - k][j + k] for k in range(4)]
                if seRepite(diagonal_secundaria):
                    return True
                
        return False

    def seRepite(listaReducida):
        for i in range(len(listaReducida) - 3):
            if listaReducida[i:i+4] == ['A', 'A', 'A', 'A'] or \
            listaReducida[i:i+4] == ['C', 'C', 'C', 'C'] or \
            listaReducida[i:i+4] == ['G', 'G', 'G', 'G'] or \
            listaReducida[i:i+4] == ['T', 'T', 'T', 'T']:
                return True
        return False

    matriz = []
    
    print("Ingrese la matriz de secuencia ADN a continuación: ")
    
    for i in range(6):
        fila = []
        for j in range(6):
            elemento = input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): ")
            fila.append(elemento)
        matriz.append(fila)

    if isMutant(matriz):
        print("¡¡MUTANTE ENCONTRADO!!")
        print("Se encontró una repetición de 4 letras consecutivas.")
    else:
        print("No se encontraron repeticiones de 4 letras consecutivas.")
        
    print("Desea ingresar otra secuencia de ADN? S / N")
    seguir = input()
