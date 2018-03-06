#!/usr/bin/python3
#encoding: utf-8

import os
import sys

# Script criado para consulta de domínios na zona de DNS

caminho = "/etc/namedb/dba/"
dir = os.listdir( caminho )

ip = raw_input('Insira o IP aqui: ')

for nome in dir:
	arquivo = open(caminho + nome, 'r')
	texto = arquivo.read()
	arquivo.close()

	if ip in texto:
		dominio = nome.replace(".db","")
		print(dominio)