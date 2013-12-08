#!/usr/bin/env python

import sys

class fabrica_t:
	
	def __init__(self, id, esquina, horario_apertura, horario_cierre):
		self.id = id
		self.esquina = esquina
		self.horario_apertura = horario_apertura
		self.horario_cierre = horario_cierre
		self.juguetes = []
	
	def insertarJuguete(self, j):
		self.juguetes.append(j)
