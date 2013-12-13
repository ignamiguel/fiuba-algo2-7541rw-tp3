#!/usr/bin/env python

class vertice_t:
	
	def __init__(self, id, x, y, latitud, longitud):
		self.id = id
		self.x = x
		self.y = y
		self.latitud = latitud
		self.longitud = longitud
		self.vecinos = []	
	
	def agregarVecino(self, v):
		if(v in self.vecinos):
			return
		
		self.vecinos.append(v)
		

