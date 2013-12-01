#!/usr/bin/env python

import sys


class esquina_t:
	
	def __init__(self, id, x, y, latitud, longitud):
		self.adyacentes = []
		self.id = id
		self.x = x
		self.y = y
		self.latitud = latitud
		self.longitud = longitud
		
	def agregarAdyacente(self, a):
		if (a in self.adyacentes):
			return false
		self.adyacentes.append(a)
		




class calle_t:
	
	def __init__(self, id, esquina_inicial, esquina_final):
		self.id = id
		self.inicio = esquina_inicial
		self.final = esquina_final


class grafo_t:
		
	def __init__(self):
		self.vertices = []
		self.aristas = []
	
	def agregarVertice(self, v):
		self.vertices.append(v)
	
	def agregarArista(self, a):
		self.aristas.append(a)
		
		for v in self.vertices:
			if (v.id == a.inicio):
				v.agregarAdyacente(a)
	
	# Agregar la arista al vertice correspondiente
	
	

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


# Abro el archivo del mapa
fmapa = open(arch_mapa,'r')

# Las esquinas del mapa son vertices
cantidad_esquinas = fmapa.readline()

grafo = grafo_t()

# Leo n veces para almacenar las esquinas
for x in range(0,int(cantidad_esquinas)):
	linea = fmapa.readline()
	campos = linea.split(',')
	e = esquina_t(campos[0],campos[1],campos[2],campos[3],campos[4])
	
	# Guardo las esquinas como vertices del grafo
	grafo.agregarVertice(e)

# Las calles representan aristas
cantidad_calles = fmapa.readline()



# Leo n veces para almacenar las calles
for x in range(0,int(cantidad_calles)):
	linea = fmapa.readline()
	campos = linea.split(',')
	c = calle_t(campos[0],campos[1],campos[2])
	
	# Guardo las calles como artistar del grafo
	grafo.agregarArista(c)

fmapa.close()







