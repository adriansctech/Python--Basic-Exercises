


def main():
	
	return 0

if __name__ == '__main__':
	main()

	print "*************************************************************"
	print "**                EVALUADOR DE DNI                         **"
	print "*************************************************************"
	print "**                                                   AdriSC**"
	print "*************************************************************"
	print ""
	print "Introduce el numero del dni  :"
	dni = input()
	print "El DNI a evaluar es ;", dni
	lista={0:'T',1:'R',2:'W',3:'A',4:'G',5:'M',6:'Y',7:'F',8:'P',9:'D', 10:'X',11:'B',12:'N',13:'J',14:'Z',15:'S',16:'Q',17:'V',18:'H',19:'L',20:'C',21:'K',22:'E'}
	resultado = dni % 23
	print "******************************************"
	print "**      La letra que corresponde es: ", lista[resultado], "**"
	print "******************************************"
