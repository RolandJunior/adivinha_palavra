# -*- coding: utf-8 -*-

import random
from collections import Counter

def seleciona_letra(dic):
    return Counter(''.join(dic)).most_common(1)[0][0]
    # Converte dicionário numa string contínua (join)
    # Pega a letra mais comum (Counter.most_common)
    # Retorno é uma lista de tuplas (letra,quant) - no caso uma só
    # Separa letra da tupla ([0][0])
##### ADICIONAR VERIFICAÇÃO DE LETRAS JÁ USADAS

def testa_letra(letra):
    if palavra.find(letra) == -1: #Marca letra errada
        erros += 1
        erradas.append(letra)
    else: #Acha posição de letra certa
        for caracter in range(num_caracteres):
            if letra == palavra[caracter]:
                resultado[caracter] = letra
    print(resultado)

with open('dicionario.txt') as arquivo:
    dicionario = arquivo.read().splitlines()

palavra = random.choice(dicionario)
num_caracteres = len(palavra)

dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]

tentativas = erros = 0
erradas = []
c = '_'
resultado = list(c * num_caracteres)
#while resultado.count(c) > 0:
    #tentativas += 1
    #seleciona_letra()
    #testa_letra()
    #limpa_dicionario()

l = seleciona_letra(dic_filtrado)
testa_letra(l)
print(palavra, l)

#resultado = ''.join(resultado)