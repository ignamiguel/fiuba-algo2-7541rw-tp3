#!/usr/bin/env python

import sys
import heapq
import math

from mapa import *


def darFormatoHora(n):		
	horas = n/60
	minutos = n - (horas * 60)
	
	if(horas < 10):
		h = "0{0}".format(horas)
	else:
		h = "{0}".format(horas)
	
	if(minutos < 10):
		m = "0{0}".format(minutos)
	else:
		m = "{0}".format(minutos)
	
	return "{0}:{1}".format(h,m)

def distanciaEntreVertices(a,b):	
	
	# print "Calculando distancia desde [{0}] a [{1}]".format(a.id, b.id)
	
	# Calcula distancia desde un
	# vertice A y otro B
	x = b.x - a.x
	y = b.y - a.y	
	
	# print "Las coordenadas son x={0} y={1}".format(x, y)
	# print "Distancia {0}".format(math.sqrt(math.pow(x,2) + math.pow(y,2)))
	# print "Presione una tecla para continuar..."
	# raw_input()		
	
	return math.sqrt(math.pow(x,2) + math.pow(y,2))	

class grafo_t:
		
	def __init__(self):
		self.vertices = [None]
		self.poloNorte = None
	
	def agregarVertice(self, id, x, y, latitud, longitud):
		# Creo un vertice
		v = vertice_t(id, x, y, latitud, longitud)		
		
		# Lo agrego a la lista
		self.vertices.append(v)
	
	def agregarArista(self, id, origen, destino):		
		# Busco el vertice de origen			
		v = self.vertices[origen]
		
		# Busco el vertice destino		
		w = self.vertices[destino]		
		
		# Las calles son doble mano
		v.agregarVecino(w)
		w.agregarVecino(v)	
		
	def ubicarPoloNorte(self, idEsquinaPoloNorte):
		# Busco el vertice donde se ubica el Polo Norte
		v = self.vertices[idEsquinaPoloNorte]	
		if(v == None):
			return False	
		
		self.poloNorte = v
		return True
			
	# Camino Optimo
	def calcularCaminoOptimo(self,vertice_id):		
		# Identifico el destino
		destino = self.vertices[vertice_id]
		if(destino == None):
			print "Error: la esquina con id {0} no existe".format(vertice_id)
			return
		
		# Defino una distancia infinita
		INFINITO = sys.float_info.max
		
		# Declaro un vector de distancias
		# inicializado en infinto
		Distancia = [INFINITO for x in xrange(len(self.vertices))]		
		
		# Declaro un vector de padres
		# inicializado en -1
		Padres = [-1 for x in xrange(len(self.vertices))]
		
		# Declaro un vector de visitados
		# inicializado en False
		Visitados = [False for x in xrange(len(self.vertices))]
		
		# Obtengo el indice del Polo Norte
		indicePolo = self.vertices.index(self.poloNorte)				
		
		# Configuro la distancia al Polo Norte en 0
		Distancia[indicePolo] = 0		
		
		# Declaro un heap de minima
		h = []
		
		# Declaro un tuple para agregar al heap
		# y la prioridad es la distancia
		origen = [Distancia[indicePolo], self.poloNorte]	
		
		# Agrego el tuple al heap 
		# para ser procesado
		heapq.heappush(h, origen)		
		
		# Proceso todos los nodos de la cola
		while len(h) != 0:			
				
			# Extraigo el de menor distancia
			u_tuple = heapq.heappop(h)			
			
			u = u_tuple[1]		
			
			indice_u = self.vertices.index(u)						
			
			if(Visitados[indice_u]):
				continue			
			
			# Lo marco como visitado
			Visitados[indice_u] = True	
			
			# Proceso todos los vertices adyacentes			
			for vecino in u.vecinos:				
				alt = Distancia[indice_u] + distanciaEntreVertices(u,vecino)
							
				indice_v = self.vertices.index(vecino)
			
				if(alt < Distancia[indice_v]):					
					Distancia[indice_v] = alt
					Padres[indice_v] = indice_u
					if(Visitados[indice_v] == False):
						v_tuple = [Distancia[indice_v], vecino]
						heapq.heappush(h, v_tuple)
			
			if(u == destino):
				# print "Se porceso el nodo destino, deberia terminar"
				break							
			
			
		# Obtengo el indice
		indice_destino = self.vertices.index(destino)
		
		metros = Distancia[indice_destino]
		
		if(metros == sys.float_info.max):
			print "Distancia es infinita"
			return		
		
		print "Distancia: {0} metros".format(int(metros))	
		
		# Mostrar el camino
		camino= []
		indice_padre = indice_destino
		
		while indice_padre != -1:
			v = self.vertices[indice_padre]
			if(v == None):
				print "Error: la esquina con id {0} no existe".format(str(indice_padre))	 
			
			camino.append(v)
			indice_padre = Padres[indice_padre]
			
		for w in reversed(camino):
			print "{0}, {1}".format(w.latitud, w.longitud)
						
