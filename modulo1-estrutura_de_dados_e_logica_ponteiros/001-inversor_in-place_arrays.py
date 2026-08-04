from random import randint

lista = [0] * 10 
for i in range(10):
    lista[i] = randint(0, 1000)

print(f"Lista original: {lista}\n")

p1 = 0
p2 = len(lista) - 1

while p2 > p1:
    c = lista[p1]
    
    lista[p1] = lista[p2]
    lista[p2] = c
        
    p1 += 1
    p2 -= 1

print(f"Lista invertida: {lista}\n")

# variaveis p1 e p2 necessarias para o problema -> espaco O(1)
# loop while -> O(n) -> vai funcionar n vezes de forma linear
# variavel c -> espaco O(1) -> é necessario? tem alguma solucao que nao precise
# acessar e editar lista e valores -> O(1)?