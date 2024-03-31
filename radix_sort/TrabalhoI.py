def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Teste do algoritmo
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Array ordenado:", arr)

import time
import random

# Função para criar uma lista ordenada em ordem crescente
def lista_ordenada_crescente(tamanho):
    return list(range(1, tamanho + 1))

# Função para criar uma lista ordenada em ordem decrescente
def lista_ordenada_decrescente(tamanho):
    return list(range(tamanho, 0, -1))

# Função para criar uma lista desordenada com números aleatórios
def lista_desordenada(tamanho):
    return random.sample(range(1, tamanho * 10), tamanho)

# Função para criar uma lista "quase" ordenada
def lista_quase_ordenada(tamanho):
    lista = list(range(2, tamanho + 1))
    lista.insert(0, tamanho + 1)
    return lista

tamanhos = [100, 1000, 10000, 100000, 1000000]

for tamanho in tamanhos:
    print(f"Tamanho do vetor: {tamanho}")
    
    # Teste do Radix Sort
    lista = lista_ordenada_crescente(tamanho)
    start_time = time.time()
    radix_sort(lista)
    end_time = time.time()
    print(f"Radix Sort (ordenada crescente): {end_time - start_time} segundos")
    
    lista = lista_ordenada_decrescente(tamanho)
    start_time = time.time()
    radix_sort(lista)
    end_time = time.time()
    print(f"Radix Sort (ordenada decrescente): {end_time - start_time} segundos")
    
    lista = lista_desordenada(tamanho)
    start_time = time.time()
    radix_sort(lista)
    end_time = time.time()
    print(f"Radix Sort (desordenada): {end_time - start_time} segundos")
    
    lista = lista_quase_ordenada(tamanho)
    start_time = time.time()
    radix_sort(lista)
    end_time = time.time()
    print(f"Radix Sort (quase ordenada): {end_time - start_time} segundos")
