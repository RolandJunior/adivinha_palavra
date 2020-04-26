# -*- coding: utf-8 -*-

import random

# Abertura do teste
print('\nO computador tentará adivinhar uma palavra escolhida aleatoriamente de um dicionário.')
print('A única informação que ele receberá será o número de caracteres da palavra.\n')
x = input('Tecle ENTER para gerar a palavra:')

# Carrega alfabeto e gera dict para contagem de letras
with open('alfabeto.txt') as arquivo:
  alfabeto = dict.fromkeys(arquivo.read().splitlines(),0)

# Carrega dicionário e zera tentativas de adivinhação
dicionario = ['bola', 'casa', 'melancia', 'inerente', 'alemanha', 'constituicao']

# Seleciona aleatoriamente uma palavra do dicionário e calcula seu número de caracteres
palavra = random.choice(dicionario)
num_caracteres = len(palavra)
print(f'\nA palavra escolhida foi "{palavra}"" e ela tem {num_caracteres} caracteres.\n')
x = input('Tecle ENTER para começar a adivinhação:')

# Filtra as que tem o número de caracteres correto
dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]
#dic_filtrado = list(filter(lambda x: len(x)==num_caracteres, dicionario))

# Conta letras em todas as palavras e ordena alfabeto da maior pra menor quantidade
for i in dic_filtrado:
  for j in alfabeto:
    alfabeto[j] += i.count(j)
alfabeto_ordenado = {k:v for k,v in sorted(alfabeto.items(), key=lambda item: item[1], reverse=True)}

# Identifica palavra
c = '_'
resultado = list(c * num_caracteres)
tentativas = 0

for letra in alfabeto_ordenado:
  if resultado.count(c) == 0:
    break
  tentativas += 1  
  for caracter in range(num_caracteres):
    if letra == palavra[caracter]:
      resultado[caracter] = letra

resultado = ''.join(resultado)
print(f'\nA palavra é "{resultado}" e foram testadas {tentativas} letras diferentes.')

