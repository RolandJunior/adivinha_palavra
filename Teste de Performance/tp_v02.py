# -*- coding: utf-8 -*-

import random, time
from collections import Counter

def seleciona_letra(dic):
    x = len(testadas)
    return Counter(''.join(dic)).most_common(x+1)[x][0]

def testa_letra(letra):
    testadas.append(letra)
    if palavra.find(letra) == -1:
        erradas.append(letra)
    else:
        for pos in range(num_caracteres):
            if letra == palavra[pos]:
                resultado[pos] = letra

with open('dicionario_reduzido.txt') as arquivo:
    dicionario = arquivo.read().splitlines()

tp_result = open('tp_v02.txt', 'w+')

p = 0
for palavra in dicionario:
    num_caracteres = len(palavra)
    t1 = time.perf_counter()
    dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]
   
    testadas = []
    erradas = []
    resultado = list('_' * num_caracteres)
    while resultado.count('_') > 0:
        testa_letra(seleciona_letra(dic_filtrado))
    resultado = ''.join(resultado)

    t2 = time.perf_counter()
    p += 1
    print(p)
    tp_result.write(f'{palavra},{num_caracteres},{t2-t1},{len(erradas)}\n')

tp_result.close()
