import sys

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

# las esquinas del mapa son vertices
fmapa = open(arch_mapa,'r')

algo = fmapa.readline()

print algo


fmapa.close()




