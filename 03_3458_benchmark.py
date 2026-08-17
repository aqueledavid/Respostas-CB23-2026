# David

import AP_03_ordenacao
import time
import random
import sys
sys.setrecursionlimit(100000)


def gerar_medio(n):
    temp = []
    for i in range(n):
        temp.append(random.randint(0,n))
    return temp

def gerar_pior(n):
    temp = []
    for i in range(n,0,-1):
        temp.append(i)
    return temp

n = 500
k = 50
dvd1,dvd2,qs1,qs2,ss1,ss2 = [],[],[],[],[],[]

testes = {}
for i in range(k):
    testes[i] = (gerar_medio(n))
testes['pior'] = (gerar_pior(n))

import copy

for i in range(5):
    lista = testes[i]
    pior = gerar_pior(n)

    t1 = time.perf_counter()
    AP_03_ordenacao.divide_and_conquer_sort(copy.copy(lista))
    dvd1.append(time.perf_counter() - t1)

    t1 = time.perf_counter()
    AP_03_ordenacao.divide_and_conquer_sort(copy.copy(pior))
    dvd2.append(time.perf_counter() - t1)

    t1 = time.perf_counter()
    AP_03_ordenacao.quick_sort(copy.copy(lista))
    qs1.append(time.perf_counter() - t1)

    t1 = time.perf_counter()
    AP_03_ordenacao.quick_sort(copy.copy(pior))
    qs2.append(time.perf_counter() - t1)

    t1 = time.perf_counter()
    AP_03_ordenacao.selection_sort(copy.copy(lista))
    ss1.append(time.perf_counter() - t1)

    t1 = time.perf_counter()
    AP_03_ordenacao.selection_sort(copy.copy(pior))
    ss2.append(time.perf_counter() - t1)

print(f'''
Média final de {k} tentativas no algoritimo "Merge Sort"
Caso médio: {sum(dvd1)/k:.6f} segundos
Pior caso: {sum(dvd2)/k:.6f} segundos

Média final de {k} tentativas no algoritimo "Quick Sort"
Caso médio: {sum(qs1)/k:.6f} segundos
Pior caso: {sum(qs2)/k:.6f} segundos

Média final de {k} tentativas no algoritimo "Selection Sort"
Caso médio: {sum(ss1)/k:.6f} segundos
Pior caso: {sum(ss2)/k:.6f} segundos
 ''')