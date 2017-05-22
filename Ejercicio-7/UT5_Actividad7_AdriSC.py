
def main():
	
	return 0

if __name__ == '__main__':
	main()
	
	print "Introduce el numero de palabras"
	numeropalabras = input()	
	contador = 0
	palabras = []
	while contador < numeropalabras:
		print"Introduce la palabra"
		palabra = raw_input()
		palabras.append(palabra)
		contador = contador+1
	print "Fin de pedir palabras"
	print ""
	contador = 0
	
	print "Vamos a mostrar las palabras de la lista"	
	print palabras
	
	print ""
	print "Que palabra deseas borrar "
	borrapalabra = raw_input()
	contador = 0
	if borrapalabra in palabras:
		print "Se va a borrar la palabra :", borrapalabra		
		palabras.remove(borrapalabra)
		print "Vamos a mostrar las palabras de la lista"
		print palabras	
	else:
		print "La palabra no esta dentro de la lista"
		print "Se va a cerrar el programa "
	
	
	
	
