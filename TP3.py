#!/usr/bin/env python

import sys
import heapq
import math

from gestor import *

""" *********************************************************
							UTILS
********************************************************* """

def obtenerComandoConParams(texto):
	partes = texto.split(' ')
	return partes

def obtenerParams(texto):
	partes = texto.split(',')	
	return partes
		
# Defino constantes
CANT_ARGS = 6
INPUT_CAPACIDAD = 1
INPUT_POLO_NORTE = 2
INPUT_ARCHIVO_FABRICAS = 3
INPUT_ARCHIVO_JUGUETES = 4
INPUT_ARCHIVO_MAPA = 5
					
""" ********************************************************* 
							MAIN
********************************************************* """

if len(sys.argv) < CANT_ARGS:
	print 'ERROR: Faltan argumentos'
	quit()

# Leo la capacidad del trineo
capacidad = sys.argv[INPUT_CAPACIDAD]

esquina_polo_norte = sys.argv[INPUT_POLO_NORTE]
arch_fabricas = sys.argv[INPUT_ARCHIVO_FABRICAS]
arch_juguetes = sys.argv[INPUT_ARCHIVO_JUGUETES]
arch_mapa = sys.argv[INPUT_ARCHIVO_MAPA]

# Creo un gestor
gestor = gestor_t()

# Defino la capacidad del trineo
gestor.definirCapacidadTrineo(capacidad)

# Abro el archivo del mapa
fmapa = open(arch_mapa,'r')

# Leo la cantidad de esquinas
# convierto la cantidad a int
cantidad_esquinas = int(fmapa.readline().rstrip())

# Leo "cantidad_esquinas" veces para almacenar las esquinas
for x in range(cantidad_esquinas):
	linea = fmapa.readline()	
	campos = linea.split(',')
	
	# Defino los campos
	ESQUINA_ID = 0
	ESQUINA_COORD_X = 1
	ESQUINA_COORD_Y = 2
	ESQUINA_LATITUD = 3
	ESQUINA_LONGITUD = 4	
	
	gestor.agregarEsquina(campos[ESQUINA_ID], campos[ESQUINA_COORD_X], campos[ESQUINA_COORD_Y], campos[ESQUINA_LATITUD], campos[ESQUINA_LONGITUD].rstrip())	

# Leo la cantidad de calles
# convierto la cantidad a int
cantidad_calles = int(fmapa.readline().rstrip())

# Leo "cantidad_calles" veces para procesar las calles
for x in range(int(cantidad_calles)):
	linea = fmapa.readline()
	campos = linea.split(',')
	
	# Defino los campos
	CALLE_ID = 0
	CALLE_ESQUINA_INICIAL = 1
	CALLE_ESQUINA_FINAL = 2
	
	gestor.agregarCalle(campos[CALLE_ID], campos[CALLE_ESQUINA_INICIAL], campos[CALLE_ESQUINA_FINAL].rstrip())	

# Cierro el archivo del mapa
fmapa.close()

# Ubico el Polo Norte
if gestor.agregarPoloNorte(esquina_polo_norte) == False:
	print "ERROR: La esquina {0} ingresada para el Polo Norte no existe".format(esquina_polo_norte)
	quit()

# Abro el archivo fabricas
ffab = open(arch_fabricas,'r')

for line in ffab:
	campos = line.split(',')
	
	# Defino los campos
	FABRICA_ID = 0
	FABRICA_ESQUINA_ID = 1
	FABRICA_HORARIO_ENTRADA = 2
	FABRICA_HORARIO_SALIDA = 3	
	
	gestor.agregarFabrica(campos[FABRICA_ID], campos[FABRICA_ESQUINA_ID], campos[FABRICA_HORARIO_ENTRADA], campos[FABRICA_HORARIO_SALIDA].rstrip())
	
# Cierro el archivo de fabricas
ffab.close()

# Abro el archivo de juguetes
fjug = open(arch_juguetes,'r')

for line in fjug:
	campos = line.split(',')
	
	# Defino los campos
	JUGUETE_FABRICA_ID = 0
	JUGUETE_ID = 1
	JUGUETE_VALOR = 2
	JUGUETE_PESO = 3
	
	gestor.agregarJuguete(campos[JUGUETE_FABRICA_ID], campos[JUGUETE_ID], campos[JUGUETE_VALOR], campos[JUGUETE_PESO].rstrip())	

# Cierro el archivo de juguetes
fjug.close()

# Procesar comando
try:	
    entrada = raw_input()
    while entrada != None:
		# Defino los campos
		COMANDO = 0
		PARAMETROS = 1
		FABRICA_ID = 0	
			
		comandoConParams = obtenerComandoConParams(entrada)		
		comando = comandoConParams[COMANDO]				
		
		if(comando == "listar_fabricas"):
			imprimir_resultado = True
			gestor.listarFabricas(imprimir_resultado)
		
		elif(comando == "valuar_juguetes"):
			params = obtenerParams(comandoConParams[PARAMETROS])
			gestor.valuarJuguetes(params[FABRICA_ID], True)
		
		elif(comando == "valuar_juguetes_total"):
			gestor.valuarJuguetesTotal()
		
		elif(comando == "camino_optimo"):
			param = obtenerParams(comandoConParams[PARAMETROS])
			gestor.obtenerCaminoOptimo(param[FABRICA_ID])
		
		entrada = raw_input()
except EOFError:
    quit()

