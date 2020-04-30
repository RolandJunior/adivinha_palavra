# -*- coding: utf-8 -*-

import random, time

with open('alfabeto.txt') as arquivo:
    alfabeto = dict.fromkeys(arquivo.read().splitlines(),0)
with open('dicionario_reduzido.txt') as arquivo:
    dicionario = arquivo.read().splitlines()

tp_result = open('tp_v01.txt', 'w+')

p = 0
for palavra in dicionario:
    num_caracteres = len(palavra)
    t1 = time.perf_counter()
    dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]
    
    for i in dic_filtrado:
        for j in alfabeto:
            alfabeto[j] += i.count(j)
    alfabeto_ordenado = {k:v for k,v in sorted(alfabeto.items(), key=lambda item: item[1], reverse=True)}
    
    c = '_'
    resultado = list(c * num_caracteres)
    tentativas = erros = 0
    erradas = []
    for letra in alfabeto_ordenado:
        if resultado.count(c) == 0: #Sai se já achou todas as letras
            break
        tentativas += 1
        if palavra.find(letra) == -1: #Marca letra errada
            erros += 1
            erradas.append(letra)
        else: #Acha posição de letra certa
            for caracter in range(num_caracteres):
                if letra == palavra[caracter]:
                    resultado[caracter] = letra
    resultado = ''.join(resultado)

    t2 = time.perf_counter()
    p += 1
    print(p)
    tp_result.write(f'{palavra},{num_caracteres},{t2-t1},{len(erradas)}\n')

tp_result.close()
    


