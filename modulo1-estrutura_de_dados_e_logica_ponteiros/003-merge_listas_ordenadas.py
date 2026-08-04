import time

start_time = time.time()

lista1 = [2, 4, 5, 6, 8, 10, 20]
lista2 = [1, 2, 3, 4, 5, 6, 7]
print(f"\nPrimeira lista ordenada: {lista1}")
print(f"Segunda lista ordenada: {lista2}\n")

lista_nova = lista1 + lista2
print(f"Lista nova: {lista_nova}\n")

# merge sort
def merge(left, right):
    if len(left) == 0:
        return right
    
    if len(right) == 0:
        return left
    
    result = []
    index_left = index_right = 0
    
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        
        if index_right == len(right):
            result += left[index_left:]
            break
        
        if index_left == len(left):
            result += right[index_right:]
            break
    
    return result  

def merge_sort(array):
    if len(array) < 2:
        return array
    
    midpoint = len(array) // 2
    
    return merge(
        left = merge_sort(array[:midpoint]),
        right = merge_sort(array[midpoint:])
    )

print(f"Lista nova ordenada com merge sort: {merge_sort(lista_nova)}")
final_time_ms = time.time() 
print(f"Tempo de execucao MERGE SORT: {final_time_ms - start_time}s\n")

# insertion sort
start_time_is = time.time() 

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        
        j = i - 1
        
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = key_item
    
    return array

print(f"Lista nova ordenada com insertion sort: {insertion_sort(lista_nova)}")
final_time = time.time()
print(f"Tempo de execucao INSERTION SORT: {final_time - start_time_is}s\n")

# merge sort -> ir dividindo uma lista recursivamente ate ter um monte de listas unitarias. Ir comparando e unindo elas
# time complexity: O(nlogn)
# duas funcoes:
#   a primeira recebe as duas listas, compara cada valor e une as listas ordenadas em uma nova
#   a segunda é a funcao recursiva, que vai dividindo a lista ate termos varias listas unitarias indivisiveis
# usando o merge sort, acho que nao tem nada para otimizar

# insertion sort -> pega a partir do segundo elemento e compara com todo o restante da lista a direita para achar o lugar certo
# na pior das hipoteses tem que comparar cada numero com todos da lista, entao: O(n2)

# considerando os outros sorting algorithms, todos parecem rodar em O(nlogn) no pior dos casos, entao nao parece ter nada para otimizar
# para conjuntos pequenos, bubble e insertion sort podem mais rapidos, mas caso eu quisesse escalar meus dados, o merge continua sendo a melhor opcao
#   apos teste, vi que o merge ainda é mais rapido
