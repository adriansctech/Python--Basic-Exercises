def letras(letra, frase):
	letra1=frase.count(letra)
	if letra1>0:
		outfile.write("La '")
		outfile.write(letra)
		outfile.write("' se ha repetido :")
		outfile.write(str(letra1))
		outfile.write(" veces.")
		outfile.write("\n")		

def main():
	
	return 0

if __name__ == '__main__':
	try:
		main()
		abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
		print "******************************************************************"
		print "*                       UT5_ACTIVIDAD13                          *"
		print "******************************************************************"
		print "*                                                    AdriSC      *"
		print "******************************************************************"
		print "*Introduce el nombre del fichero donde se guardara la informacion*"
		fichero = raw_input()		
		outfile = open(fichero, 'w')
		print "* Introduce un string :                                          *"
		frase = raw_input().lower()
		for i in abecedario:
			letras(i,frase)
		print "*      la informacion ha sido alamacenada en el fichero !!!      *"
		print "******************************************************************"
		outfile.close()
	except IOError:
		print "******************************************************************"
		print "* ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR  ERROR   *"
		print "******************************************************************"
		print "*                El fichero no existe                            *"
		print "******************************************************************"
