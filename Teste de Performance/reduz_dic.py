# -*- coding: utf-8 -*-

with open('dicionario.txt') as arquivo:
    dicionario = arquivo.read().splitlines()
    
dic_reduc = open('dicionario_reduzido.txt', 'w+')

i = 10
while i < len(dicionario):
    dic_reduc.write(f'{dicionario[i]}\n')
    i += 100