#!/usr/bin/env python

import sys
import heapq

from prueba import *


def hacer_algo(var):
	if(var == True):
		print "Es Verdad"
	else:
		return
	
	print "TERMINE"
	
fabrica_1 = fabrica_t("2580","14","0","30")
fabrica_2 = fabrica_t("2581","2562","27","75")

"""
if(fabrica_1 > fabrica_2):
	print "fabrica 1 es mayor"
else:
	print "ahora fabrica 2 es mayor"

l = []

l.append(fabrica_1)
l.append(fabrica_2)

heapq.heapify(l)

while len(l) != 0:
	print heapq.heappop(l)

"""
capacidad = 4
n = 4
V = [0,1,4,3]
W = [0,1,3,2]

A = [[0 for x in xrange(capacidad + 1)] for x in xrange(n)]


for i in range(n):
	for j in range(1,capacidad + 1):
		if(W[i] > j):
			A[i][j] = A[i - 1][j]
		else:
			A[i][j] = max(A[i - 1][j], V[i] + A[i - 1][j - W[i]])		
		
print A



