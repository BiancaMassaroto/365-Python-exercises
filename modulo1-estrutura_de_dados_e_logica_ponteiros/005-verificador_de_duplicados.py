lista = [1, 2, 3, 4, 3, 6, 2, 8, 7, 9]

# retorna o numero repetido e os indices onde eles se encontram
hashmap = {}
dupes = {}

def check_dupes(lista):
    for i in range(len(lista)):
        if lista[i] in hashmap:
            dupes[lista[i]] = [hashmap[lista[i]], i]
        else:
            hashmap[lista[i]] = i
    
    return dupes

print(check_dupes(lista))

# retorna apenas o numero repetido
hashset = set()
valores = []

for i in range(len(lista)):
    if lista[i] in hashset:
        valores.append(lista[i])
    else:
        hashset.add(lista[i])

print(valores)

# OBS: acessar/verificar informacoes em um hashset/hashmap é feito em tempo constante (sem colisoes) -> O(1)