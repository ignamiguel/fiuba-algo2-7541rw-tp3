#!/usr/bin/env python

import sys
import heapq

from fabrica import *
from juguete import *
from grafo import *


class esquina_t:
	
	def __init__(self, id, x, y, latitud, longitud):
		self.adyacentes = []
		self.id = id
		self.x = x
		self.y = y
		self.latitud = latitud
		self.longitud = longitud
		self.fabrica = None
		
	def agregarAdyacente(self, a):
		if (a in self.adyacentes):
			return false
		self.adyacentes.append(a)
		
	def ubicarFabrica(self, f):
		self.fabrica = f


class calle_t:
	
	def __init__(self, id, esquina_inicial, esquina_final):
		self.id = id
		self.inicio = esquina_inicial
		self.final = esquina_final



""" *********************************************************
							UTILS
********************************************************* """

def obtenerComandoConParams(texto):
	partes = texto.split(' ')
	return partes

def obtenerParams(texto):
	partes = texto.split(',')	
	return partes
		
					
""" ********************************************************* 
							MAIN
********************************************************* """
#define CANT_ARGS
CANT_ARGS = 6

if len(sys.argv) < CANT_ARGS:
	print 'ERROR: faltan argumentos'
	quit()

capacidad = sys.argv[1]
id_esquina_polo_norte = sys.argv[2]
arch_fabricas = sys.argv[3]
arch_juguetes = sys.argv[4]
arch_mapa = sys.argv[5]

# Creo un grafo
grafo = grafo_t()

# Ubico el Polo Norte
grafo.ubicarPoloNorte(id_esquina_polo_norte)

# Defino la capacidad del trineo
capacidad = capacidad.replace('#','')

grafo.agregarCapacidadTrineo(int(capacidad))


# Abro el archivo del mapa
fmapa = open(arch_mapa,'r')

# Las esquinas del mapa representan vertices
cantidad_esquinas = fmapa.readline()


# Leo "cantidad_esquinas" veces para almacenar las esquinas
for x in range(0,int(cantidad_esquinas)):
	linea = fmapa.readline()
	campos = linea.split(',')
	e = esquina_t(campos[0],campos[1],campos[2],campos[3],campos[4].rstrip())
	
	# Guardo las esquinas como vertices del grafo
	grafo.agregarVertice(e)

# Las calles representan aristas
cantidad_calles = fmapa.readline()

# print "Listo Vertices"

# Leo "cantidad_calles" veces para almacenar las calles
for x in range(0,int(cantidad_calles)):
	linea = fmapa.readline()
	campos = linea.split(',')
	c = calle_t(campos[0],campos[1],campos[2].rstrip())
	
	# Guardo las calles como artistar del grafo
	grafo.agregarArista(c)

fmapa.close()

# Agrego las fabricas
ffab = open(arch_fabricas,'r')
for line in ffab:
	campos = line.split(',')
	f = fabrica_t(campos[0], campos[1], campos[2], campos[3].rstrip())
	grafo.agregarFabrica(f)

ffab.close()


# Agrego los juguetes

fjug = open(arch_juguetes,'r')
for line in fjug:
	campos = line.split(',')
	j = juguete_t(campos[1], campos[0],campos[2],campos[3].rstrip())
	grafo.agregarJuguete(j)

fjug.close()

# Obtener comando
try:	
    entrada = raw_input()
    while entrada != None:		
		comandoConParams = obtenerComandoConParams(entrada)		
		comando = comandoConParams[0]				
		
		if(comando == "listar_fabricas"):
			grafo.listarFabricas()
		
		elif(comando == "valuar_juguetes"):
			params = obtenerParams(comandoConParams[1])
			grafo.valuarJuguetes(params[0])
		
		entrada = raw_input()
except EOFError:
    quit()




	




