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

# Carrega dicionário e conta palavras
with open('dicionario.txt') as arquivo:
    dicionario = arquivo.read().splitlines()
    p = f'{len(dicionario):,}'.replace(',','.') 

# Abertura do teste
print(f'\nO computador tentará adivinhar uma palavra escolhida aleatoriamente de um dicionário de {p} palavras.')
print('A única informação que ele receberá será o número de caracteres da palavra.')
x = input('Tecle ENTER para gerar a palavra:')

# Seleciona aleatoriamente uma palavra do dicionário e calcula seu número de caracteres
palavra = random.choice(dicionario)
num_caracteres = len(palavra)
print(f'A palavra escolhida foi "{palavra}"" e ela tem {num_caracteres} caracteres.')
x = input('Tecle ENTER para começar a adivinhação:')

# Inicia timer
t1 = time.perf_counter()

# Filtra as palavras que tem o número de caracteres correto
dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]

# Identifica a palavra
testadas = []
erradas = []
resultado = list('_' * num_caracteres)
while resultado.count('_') > 0:
    letra = seleciona_letra(dic_filtrado)
    letra_stat = testa_letra(letra)
    # Remove do dicionário palavras com letras erradas
    if letra_stat == 1: 
        dic_filtrado = [i for i in dic_filtrado if letra not in i]

# Mostra resultados
resultado = ''.join(resultado)
t2 = time.perf_counter()
print(f'A palavra é "{resultado}"')
print(f'O programa gastou {t2-t1:.4f} segundos para adivinhá-la.')
print(f'Foram testadas {len(testadas)} letras e {len(erradas)} estavam erradas: {", ".join(erradas)}')
