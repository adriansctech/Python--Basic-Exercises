


def main():
	
	return 0

if __name__ == '__main__':
	try:
		main()
		print "*********************************************************"
		print "*    VAMOS A DARLE AL VUELTA COMPLETA A UN FICHERO      *"
		print "*********************************************************"
		print "*                                                       *"
		print "*            SOMOS ASI DE GRACIOSOS                     *"
		print "*********************************************************"
		print "Introduce la ruta del fichero"
		fichero = raw_input()		
		infile = open(fichero,'r')
		for line in infile:			
			print line[::-1]
		infile.close()
		print "***  Gracias por aguantarnos  ***"
	except IOError:
		print "El fichero no existe"
		print "***  Gracias por aguantarnos  ***"
		
