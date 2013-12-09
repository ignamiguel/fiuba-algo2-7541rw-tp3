#!/usr/bin/env python

class esquina_t:
	
	def __init__(self, id, x, y, latitud, longitud):
		self.calles = []
		self.id = id
		self.x = x
		self.y = y
		self.latitud = latitud
		self.longitud = longitud
		self.fabrica = None
		
	def agregarCalle(self, a):
		if (a in self.calles):
			return
			
		self.calles.append(a)
		
	def ubicarFabrica(self, f):
		self.fabrica = f
		
class calle_t:
	
	def __init__(self, id, esquina_inicial, esquina_final):
		self.id = id
		self.inicio = esquina_inicial
		self.final = esquina_final
