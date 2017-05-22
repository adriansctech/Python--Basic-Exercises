
def main():
	
	return 0

if __name__ == '__main__':
	main()
	totalsegundos =int(input("Introduce el total de segundos :"))
	
	horas = int(totalsegundos/3600)		
	minutos = int((totalsegundos-(horas*3600))/60)
	segundos = totalsegundos- ((horas*3600)+(minutos*60))
	print "El total es de ", horas, "horas ", minutos, ", minutos y ", segundos, "segundos. "	
	

