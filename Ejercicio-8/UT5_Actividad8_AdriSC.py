
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
	palabras.sort()
	print "Vamos a mostrar la lista ordenada"
	print palabras

