def cria_mariz_2d(n_linhas, n_colunas):
    mat = []
    
    for i in range(n_linhas):
        l = []
        
        for j in range(n_colunas):
            valor = input(f"Digite um valor para a posicao {[i, j]}: ")
            l.append(valor)
        
        mat.append(l)
    
    return mat

def transposta(matriz):
    matriz_transposta = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz_transposta[j][i] = matriz[i][j]
    
    return matriz_transposta

matriz = cria_mariz_2d(4, 3)

for i in range(len(matriz)):
    print(matriz[i])

print(transposta(matriz))