import random

lista = [random.randint(1, 100) for i in range(random.randint(0, 5))]

def gerar_lista(tamanho):
    lista = []
    
    for i in range(tamanho):
        lista.append([])
    
    return lista

def tabela_hash(lista, valores):
    for i in range(len(valores)):
        indice = valores[i] % len(lista)
        lista[indice].append(valores[i])
    
    return lista

lista_vazia = gerar_lista(len(lista))

print(lista)
print(tabela_hash(lista_vazia, lista))
