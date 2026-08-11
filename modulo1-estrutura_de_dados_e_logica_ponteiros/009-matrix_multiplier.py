def cria_mariz_2d(n_linhas, n_colunas):
    mat = []
    
    for i in range(n_linhas):
        l = []
        
        for j in range(n_colunas):
            valor = input(f"Digite um valor para a posicao {[i, j]}: ")
            l.append(valor)
        
        mat.append(l)
    
    return mat

def multiplica_matriz(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return "Erro: O número de colunas da Matriz 1 deve ser igual ao número de linhas da Matriz 2."
    
    mult = [[0 for _ in range(len(matriz1))] for _ in range(len(matriz2[0]))]
    
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            soma_produto = 0
            for k in range(len(matriz2)):
                soma_produto += float(matriz1[i][k]) * float(matriz2[k][j])
            mult[i][j] = soma_produto
    
    return mult

matriz1 = cria_mariz_2d(2, 2)
matriz2 = cria_mariz_2d(2, 2)

print(multiplica_matriz(matriz1, matriz2))
       