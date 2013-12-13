#!/usr/bin/env python

import sys
from juguete import *

class fabrica_t:
	
	def __init__(self, id, esquina, horario_apertura, horario_cierre):
		self.id = id
		self.esquina = esquina
		self.horario_apertura = horario_apertura
		self.horario_cierre = horario_cierre
		self.juguetes = []
	
	def insertarJuguete(self, id, valor, peso):
		# Creo un juguete
		j = juguete_t(id, valor, peso)
		
		# Agrego el juguete a la lista
		self.juguetes.append(j)
