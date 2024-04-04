import random
import time

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
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Tamanhos das listas
sizes = [100, 1000, 10000, 100000, 1000000, 10000000]

# Função para gerar listas aleatórias de inteiros
def generate_random_int_list(size):
    return [random.randint(0, 1000) for _ in range(size)]

# Função para gerar lista quase ordenada de inteiros
def generate_almost_sorted_int_list(size):
    lst = [i for i in range(size)]
    lst[0], lst[1] = lst[1], lst[0]  # Troca os dois primeiros elementos
    return lst

# Função para medir o tempo de execução do Radix Sort
def measure_radix_sort_time(arr):
    start_time = time.time()
    radix_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Cenários
scenarios = {
    "Lista ordenada em ordem crescente": lambda size: [i for i in range(size)],
    "Lista ordenada em ordem decrescente": lambda size: [i for i in range(size, 0, -1)],
    "Lista desordenada com números aleatórios": generate_random_int_list,
    "Lista quase ordenada": generate_almost_sorted_int_list
}

# Executando o comparativo
for scenario_name, scenario_generator in scenarios.items():
    print(f"== {scenario_name} ==")
    for size in sizes:
        print(f"Tamanho: {size}")
        arr = scenario_generator(size)
        time_taken = measure_radix_sort_time(arr.copy())
        print(f"Radix Sort: {time_taken:.6f} segundos")
        print()
    print()