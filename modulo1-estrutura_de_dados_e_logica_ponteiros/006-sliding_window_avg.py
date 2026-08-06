def sliding_window(k, lista):
    windowStart = 0
    windowEnd = k
    final = {}
    
    while windowEnd <= len(lista):
        soma = 0
        nums = []
        i = windowStart
        
        while i < windowEnd:
            soma = soma + lista[i]
            nums.append(i + 1)
            i += 1
            
        final[soma/k] = nums
        
        windowStart += 1
        windowEnd = windowStart + k
    
    return final

lista = [1, 2, 3, 4, 5, 6]
k = 2

print(sliding_window(k, lista))
            