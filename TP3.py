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
		self.fabrica = None
		
	def agregarAdyacente(self, a):
		if (a in self.adyacentes):
			return false
		self.adyacentes.append(a)
		
	def agregarFabrica(self, f):
		self.fabrica = f


class calle_t:
	
	def __init__(self, id, esquina_inicial, esquina_final):
		self.id = id
		self.inicio = esquina_inicial
		self.final = esquina_final


class grafo_t:
		
	def __init__(self):
		self.vertices = {}
		self.aristas = {}
		self.fabricas = {}
		self.poloNorte = None
		self.capacidadTrineo = None
	
	def agregarVertice(self, v):
		self.vertices[v.id] = v
	
	def agregarArista(self, a):
		self.aristas[a.id] = a
		
		v = self.vertices.get(a.inicio, None)
		if (v != None):
			v.agregarAdyacente(a)
				
	def agregarFabrica(self, f):
		self.fabricas[f.id] = f
		v = self.vertices.get(f.esquina, None)
		if (v != None):
			v.agregarFabrica(f)
	
	def agregarJuguete(self, j):
		f = self.fabricas.get(j.fabrica, None)
		if(f != None):
			v = self.vertices.get(f.esquina, None)
			if(v != None):
				v.fabrica.agregarJuguete(j)
	
	def ubicarPoloNorte(self, idEsquinaPoloNorte):
		self.poloNorte = idEsquinaPoloNorte
		
	
	def agregarCapacidadTrineo(self, capacidad):
		self.capacidadTrineo = capacidad


class fabrica_t:
	
	def __init__(self, id, esquina, horario_entrada, horario_salida):
		self.id = id
		self.esquina = esquina
		self.horario_entrada = horario_entrada
		self.horario_salida = horario_salida
		self.juguetes = []
	
	def agregarJuguete(self, j):
		self.juguetes.append(j)


class juguete_t:
	
	def __init__(self, id, fabrica, valor, peso):
		self.id = id
		self.fabrica = fabrica
		self.valor = valor
		self.peso = peso

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

# Las esquinas del mapa son vertices
cantidad_esquinas = fmapa.readline()



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

# Agrego las fabricas
ffab = open(arch_fabricas,'r')
for line in ffab:
	campos = line.split(',')
	f = fabrica_t(campos[0], campos[1], campos[2], campos[3])
	grafo.agregarFabrica(f)

ffab.close()


# Agrego los juguetes
fjug = open(arch_juguetes,'r')
for line in fjug:
	campos = line.split(',')
	j = juguete_t(campos[1], campos[0],campos[2],campos[3])
	grafo.agregarJuguete(j)

fjug.close()









