# -*- coding: utf-8 -*-

import random, time
from collections import Counter

def seleciona_letra(dic):
    x = 0
    while True:
        l = Counter(''.join(dic)).most_common(x+1)[x][0]
        x += 1
        if l not in testadas:
            return l            

def testa_letra(l):
    testadas.append(l)
    if palavra.find(l) == -1:
        erradas.append(l)
        return 1
    else:
        for pos in range(num_caracteres):
            if l == palavra[pos]:
                resultado[pos] = l
        return 0

with open('dicionario_reduzido.txt') as arquivo:
    dicionario = arquivo.read().splitlines()

tp_result = open('tp_v02_filtra_dic.txt', 'w+')
    
p = 0
for palavra in dicionario:
    num_caracteres = len(palavra)
    t1 = time.perf_counter()
    dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]
    
    testadas = []
    erradas = []
    resultado = list('_' * num_caracteres)
    while resultado.count('_') > 0:
        letra = seleciona_letra(dic_filtrado)
        letra_stat = testa_letra(letra)
        if letra_stat == 1: 
            dic_filtrado = [i for i in dic_filtrado if letra not in i]
    resultado = ''.join(resultado)

    t2 = time.perf_counter()
    p += 1
    print(p)
    tp_result.write(f'{palavra},{num_caracteres},{t2-t1},{len(erradas)}\n')

tp_result.close()