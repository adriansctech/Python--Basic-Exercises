palabras=[]
respuesta = None

def crearLista():
	print "Introduce el numero de palabras"
	numeropalabras = input()	
	contador = 0	
	while contador < numeropalabras:
		print"Introduce la palabra"
		palabra = raw_input()
		palabras.append(palabra)
		contador = contador+1
	print "Fin de pedir palabras"
	print ""
	print palabras
	
def ordenarLista():
	crearLista()
	palabras.sort()
	print palabras

def imprimirLista():
	if not palabras:
		print "No hay ninguna lista aun, deberas de crear una."
		crearLista()
	print palabras
	
def agregarPalabras():
	if not palabras:
		print "No hay ninguna lista aun, deberas de crear una."
		crearLista()
	print"Introduce la palabra"
	palabra = raw_input()
	palabras.append(palabra)
	imprimirLista()
	
def borrarPalabra():
	if not palabras:
		print "No hay ninguna lista aun, deberas de crear una."
		crearLista()
	print "Introduce la palabra que deseas eliminar :"
	elimina = raw_input()
	if elimina in palabras: 
		palabras.remove(elimina)
		imprimirLista()
	else:
		print "La palabra no esta en esta lista"
def main():
	
	return 0

if __name__ == '__main__':
	main()
	


	while respuesta != "x":
		print "**********************************************"
		print "*                                            *"
		print "*Crear una lista              Opcion-- c --  *"
		print "*Ordenar una lista            Opcion-- o --  *"
		print "*Imprimir lista               Opcion-- i --  *"
		print "*Agregar una palabra          Opcion-- a --  *"
		print "*Eliminar una palabra         Opcion-- e --  *"
		print "*Salir                        Opcion-- x --  *"
		print "*                                            *"
		print "**********************************************"
		print "Que deseas realizar"
		respuesta = raw_input()	
		if respuesta == "c" :
			print "Has elegido la opcion -- Cear lista  --"
			print ""
			crearLista();
		if respuesta == "o":
			print "Has elegido la opcion  -- Ordenar lista --"
			print ""
			ordenarLista();
		if respuesta == "i":
			print "Has elegido la opcion -- Imprimir lista --"
			print ""
			imprimirLista()
		if respuesta == "a":
			print "Has elegido la opcion -- Agregar una palabra --"
			print ""
			agregarPalabras()
		if respuesta == "e":
			print "Has elegido la opcion  -- Eliminar una palabra --"
			print ""
			borrarPalabra()
		if respuesta == "x":
			print "Has elegido la opcion  -- Salir --"
			print ""
			print "ADIOS"
			break;
