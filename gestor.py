#!/usr/bin/env python

from grafo import *
from fabrica import *

class gestor_t:
	
	def __init__(self):
		self.grafo = grafo_t()
		self.fabricas = []
		self.fabricas_lista = []
		# self.poloNorte = None
		self.capacidadTrineo = 0
		self.lista_optima = []

	def definirCapacidadTrineo(self, capacidad):
		# Convierto el valor a int		
		self.capacidadTrineo = int(capacidad)
		
	def agregarEsquina(self, id, x, y, latitud, longitud):
		# Convierto los valores a int y a float
		id = int(id)		
		x= float(x)		
		y = float(y)		
		latitud = float(latitud)
		longitud = float(longitud)
		
		self.grafo.agregarVertice(id, x, y, latitud, longitud)
		
	def agregarCalle(self, id, origen, destino):
		# Convierto los valores a int
		id = int(id)
		origen = int(origen)
		destino = int(destino)
		
		self.grafo.agregarArista(id, origen, destino)
	
	def agregarPoloNorte(self, id_esquina):
		# Convierto el id a int
		id_esquina = int(id_esquina)
		
		if( not self.grafo.ubicarPoloNorte(id_esquina)):
			return False
		
		return True
		
	def agregarFabrica(self, id, esquina_id, horario_entrada, horario_salida):
		# Convierto los valores a int
		id = int(id)
		esquina_id = int(esquina_id)
		horario_entrada = int(horario_entrada)
		horario_salida = int(horario_salida)
		
		# Creo una fabrica
		f = fabrica_t(id, esquina_id, horario_entrada, horario_salida)
		
		# Agrego la fabrica a la lista
		self.fabricas.append(f)		
		
		# Agrego como elementos de la lista item
		# para que la funcion sort nativa ordene
		# por estos campos
		item = []
		item.append(horario_salida)
		item.append(horario_entrada)
		item.append(id)
		
		# Agrego el item a la lista de fabricas
		self.fabricas_lista.append(item)
		
	def agregarJuguete(self, fabrica_id, id, valor, peso):
		# Convierto los valores a int
		fabrica_id = int(fabrica_id)
		id = int(id)
		valor = int(valor)
		peso = int(peso)
		
		# Agrego el juguete a la fabrica
		self.fabricas[fabrica_id].insertarJuguete(id, valor, peso)
		
	# Listar Fabricas
	def listarFabricas(self, imprimir_resultado):
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
		if(imprimir_resultado):
			print "Cantidad: {0}".format(len(self.lista_optima))
			for item in self.lista_optima:
				id = item[2]
				print "{0}, {1}, {2}".format(id,darFormatoHora(item[1]),darFormatoHora(item[0]))		
	
	# Valuar juguetes
	def valuarJuguetes(self, fabrica_id, imprimir_resultado):
		fabrica_id = int(fabrica_id)
		f = self.fabricas[fabrica_id]
		if(f == None):
			print "Error: la fabrica con id {0} no existe".format(fabrica_id)
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

		if(imprimir_resultado):
			print "Total: {0} Sonrisas".format(A[n][self.capacidadTrineo])

		# Devuelvo el valor total de sonrisas
		return A[n][self.capacidadTrineo]
		
	# Valuar juguetes Total
	def valuarJuguetesTotal(self):
		cont = 0
				
		# Si la lista optima no esta generada,
		# la genero
		if(len(self.lista_optima) == 0):
			imprimir_resultado = False
			self.listarFabricas(imprimir_resultado)
		
		for f in self.lista_optima:
			sonrisas = None
			sonrisas = self.valuarJuguetes(f[2],False)
			if(sonrisas != None):
				cont = cont + sonrisas				
		
		print "Total: {0} Sonrisas".format(cont)		
	
	# Camino Optimo	
	def obtenerCaminoOptimo(self, fabrica_id):
		fabrica_id = int(fabrica_id)
		
		# Busco la fabrica destino		
		fabrica_destino = self.fabricas[fabrica_id]
		if(fabrica_destino == None):
			print "Error: la fabrica con id {0} no existe".format(fabrica_id)
			return
		
		# Busco el vertice destino
		self.grafo.calcularCaminoOptimo(fabrica_destino.esquina)
