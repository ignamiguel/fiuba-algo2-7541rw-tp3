#!/usr/bin/env python

import sys


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


class grafo_t:
		
	def __init__(self):
		self.vertices = {}
		self.vertices_lista = []
		self.aristas = {}
		self.fabricas = {}
		self.fabricas_lista = []
		self.poloNorte = None
		self.capacidadTrineo = None
		self.lista_optima = []
	
	def agregarVertice(self, v):
		self.vertices[v.id] = v
		self.vertices_lista.append(v)
	
	def agregarArista(self, a):
		self.aristas[a.id] = a
		
		v = self.vertices.get(a.inicio, None)
		if (v != None):
			v.agregarAdyacente(a)
				
	def agregarFabrica(self, f):
		self.fabricas[f.id] = f
				
		# Busco el vertice
		v = self.vertices.get(f.esquina, None)
		if (v == None):
			print "Esquina {0} no existe".format(f.esquina)
			return
		
		v.ubicarFabrica(f)
		
		# Convierto a int los atributos de f
		# y los agrego como elementos de la lista item
		item = []
		item.append(int(f.horario_cierre))
		item.append(int(f.horario_apertura))
		item.append(int(f.id))		
		
		# Agrego el item a la lista de fabricas
		self.fabricas_lista.append(item)
	
	
	def agregarJuguete(self, j):
		f = self.fabricas.get(j.fabrica, None)
		if(f == None):
			print "Error: la fabrica con id {0} no existe".format(j.fabrica)
			return
		
		f.insertarJuguete(j)	
		
	
	def ubicarPoloNorte(self, idEsquinaPoloNorte):
		self.poloNorte = idEsquinaPoloNorte
		
	
	def agregarCapacidadTrineo(self, capacidad):
		self.capacidadTrineo = capacidad
		
		
	# Listar Fabricas
	def listarFabricas(self, imprimir):
		
		# Ordeno las fabricas por 
		# horario de cierre
		# horario de apertura
		# id
		self.fabricas_lista.sort()			
		
		# Declaro una lista para guardar las 
		# mejores opciones
		self.lista_optima = []
		
		for i in range(len(self.fabricas_lista) - 1):					
			
			if(i == 0):
				f1 = self.fabricas_lista[i]
				self.lista_optima.append(f1)
				i = i + 1
				f2 = self.fabricas_lista[i]			
			else:
				f2 = self.fabricas_lista[i]			
			
			# Comparo si el horario de apertura
			# de f2 es mayor o igual
			# al horario de cierre de f1			
			if(f2[1] >= f1[0]):
				self.lista_optima.append(f2)
				f1 = f2				
			
		# Tengo las mejores opciones
		if(imprimir):
			print "Cantidad: {0}".format(len(self.lista_optima))
			for item in self.lista_optima:
				id = item[2]
				print "{0}, {1}, {2}".format(id,darFormatoHora(item[1]),darFormatoHora(item[0]))

	# Valuar juguetes
	def valuarJuguetes(self, fabricaId, imprimir):
		f = self.fabricas.get(fabricaId, None)
		if(f == None):
			print "Error: la fabrica con id {0} no existe".format(fabricaId)
			return			
		
		# Obtengo la cantidad de juguetes
		n = len(f.juguetes)
		
		# Genero un vector W de peso y V de valor
		W = []
		V = []
		
		# El elemento nulo pesa 0
		# y su valor es 0
		W.append(0)
		V.append(0)
		
		# Agrego los pesos y los valores
		# Convierto las variables a int
		for i in range(n):
			W.append(int(f.juguetes[i].peso))
			V.append(int(f.juguetes[i].valor))		
		
		
		# Declaro una matriz A 
		# para guardar la mejor opcion
		# inicializada en 0
		A = [[0 for x in xrange(self.capacidadTrineo + 1)] for x in xrange(n + 1)]
		
		for i in xrange(1, n + 1):
			for j in xrange(1, self.capacidadTrineo + 1):				
				if(W[i] > j):
					A[i][j] = A[i - 1][j]					
				else:
					A[i][j] = max(A[i - 1][j], V[i] + A[i - 1][j - W[i]])							
		
		if(imprimir):
			print "Total: {0} Sonrisas".format(A[n][self.capacidadTrineo])
		
		return A[n][self.capacidadTrineo]
	
	# Valuar juguetes Total
	def valuarJuguetesTotal(self):
		cont = 0
				
		# Si la lista optima no esta cargada,
		# la cargo
		if(len(self.lista_optima) == 0):
			self.listarFabricas(False)
		
		for f in self.lista_optima:
			sonrisas = None
			# Convierto a string el Id de la fabrica
			# para buscarlo en el diccionario
			id = str(f[2])
			sonrisas = self.valuarJuguetes(id,False)
			if(sonrisas != None):
				cont = cont + sonrisas
				
		
		print "Total: {0} Sonrisas".format(cont)
	
	# Camino Optimo
	def obtenerCaminoOptimo(self,fabricaId):
		# Busco la fabrica
		f = self.fabricas.get(fabricaId, None)
		if(f == None):
			print "Error: la fabrica con id {0} no existe".format(fabricaId)
			return	
		
		# Defino una distancia infinita
		infinito = -1
		
		# Declaro un vector de distancias
		D = [infinito for x in xrange(len(self.vertices_lista))]
		
		# Declaro un vector de padres
		P = [0 for x in xrange(len(self.vertices_lista))]
		
		print D
		
		
		
		
		
		
		
		
		
		
		
		
