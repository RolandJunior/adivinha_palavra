# -*- coding: utf-8 -*-

import random, time

# Carrega alfabeto e gera dict para contagem de letras
with open('alfabeto.txt') as arquivo:
  alfabeto = dict.fromkeys(arquivo.read().splitlines(),0)

# Carrega dicionário
with open('dicionario.txt') as arquivo:
  dicionario = arquivo.read().splitlines()
  p = f'{len(dicionario):,}'.replace(',','.') 

# Abertura do teste
print(f'\nO computador tentará adivinhar uma palavra escolhida aleatoriamente de um dicionário de {p} palavras.')
print('A única informação que ele receberá será o número de caracteres da palavra.\n')
x = input('Tecle ENTER para gerar a palavra:')

# Seleciona aleatoriamente uma palavra do dicionário e calcula seu número de caracteres
palavra = random.choice(dicionario)
num_caracteres = len(palavra)
print(f'\nA palavra escolhida foi "{palavra}"" e ela tem {num_caracteres} caracteres.\n')
x = input('Tecle ENTER para começar a adivinhação:')

# Inicia timer
t1 = time.perf_counter()

# Filtra as que tem o número de caracteres correto
dic_filtrado = [i for i in dicionario if len(i) == num_caracteres]

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
t2 = time.perf_counter()
print(f'\nA palavra é "{resultado}" e foram testadas {tentativas} letras diferentes.')
print(f'O programa gastou {t2-t1:.4f} segundos para adivinhá-la.')

