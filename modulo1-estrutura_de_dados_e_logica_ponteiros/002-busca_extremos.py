import random

# Minha solucao para criar a lista de 10 numeros float aleatorios
# lista = [0] * 10
# for i in range(len(lista)):
    # lista[i] = random.uniform(1, 1000)

# Solucao que eu acabei encontrando na internet que achei melhor
lista = [random.uniform(0, 1000) for i in range(10)]

print(f"\nLista original: {lista}\n")

maior = lista[0]
menor = lista[0]

for i in range(len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
    elif lista[i] <= menor:
        menor = lista[i]

print(f"Maior numero da lista: {maior}")
print(f"Menor numero da lista: {menor}\n")

# descricao: ir armazenando os maiores e menores valores em uma variavel e comparando com os valores restantes
# time complexity: O(n) -> percorre a lista apenas uma vez e achar e comparar valores é feito em O(1)
# space complexity: O(1) por conta das variaveis? O(n) por conta da lista?
