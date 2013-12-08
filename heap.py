#!/usr/bin/env python

import sys

from fabrica import *

class heap_t:
	
	def __init__(self):
		self.vector = []
		self.cant = 0
		
	def comparar(self, a, b):
		if(a == None):
			return 1
			
		if(b == None):
			return -1
		
		if(a.horario_cierre < b.horario_cierre):
				return 1
		elif(a.horario_cierre > b.horario_cierre):
			return -1
		else:
			if(a.horario_apertura < b.horario_apertura):
				return 1
			elif(a.horario_apertura > b.horario_apertura):
				return -1
			else:
				if(a.id < b.id):
					return 1
				else:
					return -1
	
	def encolar(self, elemento):
		i = len(self.vector)		
		self.vector.append(elemento)
		self.upHeap(elemento,i)

	def swap(self, posA, posB):
		aux = self.vector[posA]
		self.vector[posA] = self.vector[posB]
		self.vector[posB] = aux
	
	def upHeap(self, hijo, pos_hijo):
		if(pos_hijo == 0):
			return
		
		while pos_hijo > 0:			
			pos_padre = (pos_hijo - 1) / 2
			padre = self.vector[pos_padre]
			if(self.comparar(hijo,padre) > 0):
				# swap
				self.swap(pos_hijo,pos_padre)
				pos_hijo = pos_padre
			else:
				return
	
	def estaVacio(self):
		return len(self.vector) == 0
	
	def desencolar(self):		
		if(self.estaVacio()):
			return None
		
		e = self.vector[0]
		print e.id
		
		if(self.estaVacio()):
			return e
			
		cant = len(self.vector)
		print cant
		ultimo = self.vector[cant - 1]
		self.vector[0] = ultimo
		self.downHeap()
		return e

	def obtenerPosHijoMayor(self, i):
		posHijoIzq = (i * 2) + 1
		posHijoDer = (i * 2) + 2
		
		der = None
		if(posHijoIzq < len(self.vector)):
			der = self.vector[posHijoIzq]
		
		izq = None
		if(posHijoDer < len(self.vector)):
			izq = self.vector[posHijoIzq]
		
		if(self.comparar(izq,der) > 0):
			return posHijoIzq
		else:
			return posHijoDer
		
	
	def downHeap(self):
		pos_padre = 0
		padre = self.vector[0]
		
		while (pos_padre < len(self.vector)):
			pos_hijo = self.obtenerPosHijoMayor(pos_padre)
			hijo = self.vector[pos_hijo]
			
			if(self.comparar(hijo,padre) > 0):
				self.swap(pos_padre, pos_hijo)
				pos_padre = pos_hijo
			else:
				return
