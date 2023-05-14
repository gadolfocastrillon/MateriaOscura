#def unird(n1,n2,n3):
def unird(n1,n2):
	archivo1 = open(n1) 
	archivo2 = open(n2) 
	#archivo3 = open(n3) 
	d1 = archivo1.read() 
	d2 = archivo2.read() 
	#d3 = archivo3.read() 
	archivo1.close() 
	archivo2.close() 
	#archivo3.close() 
	#return d1 + d2 + d3 
	return d1 + d2 
	
dt1 = unird("datosLikelihood-mass100-500.txt","datosLikelihood-mass70-1000.txt")
#dt2 = unird("datosLikelihood2.txt","datosLikelihood3.txt")
#dt3 = unird("datosLikelihood4.txt","datosLikelihood-modificado-P100.txt")
#dt2 = unird("datosLikelihoodP6.txt","datosLikelihoodP8.txt")
#dt2 = unird("datosLikelihood4.txt","datosLikelihood5.txt","datosLikelihood6.txt") 
#dt3 = unird("datosLikelihood7.txt","datosLikelihood8.txt","datosLikelihood9.txt") 
#dt4 = unird("datosLikelihood10.txt","datosLikelihood11.txt","DatosLikelihood.txt")



#dt = dt1 + dt2 + dt3
#dat = dt1 + dt2
archivo = open("unionDatos70-1000.txt",'w') 
archivo.write(dt1) 
#archivo.write(dt)
#archivo.write(dt1+dt2+dt3+dt4+dt5)
archivo.close()