def sliding_window(lista, alvo):
    priority_queue = []
    soma = 0
    i = 0
    
    while soma != alvo and i < len(lista):
        if lista[i] > alvo:
            priority_queue = []
            soma = 0
            i += 1
            continue
        elif alvo - soma >= lista[i]:
            priority_queue.append(lista[i])
            soma = soma + lista[i]
        else:
            soma = soma + lista[i] - priority_queue[0]
            priority_queue.pop(0)
            priority_queue.append(lista[i])
            
            while soma > alvo:
                soma = soma - priority_queue[0]
                priority_queue.pop(0)
        
        i += 1
    
    return priority_queue

lista = [1, 2, 3, 9, 1, 1, 3, 8, 6]
alvo = 10

print(sliding_window(lista, alvo))
