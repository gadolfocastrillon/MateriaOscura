def unird(n1,n2,n3):
	archivo1 = open(n1) 
	archivo2 = open(n2) 
	archivo3 = open(n3) 
	d1 = archivo1.read() 
	d2 = archivo2.read() 
	d3 = archivo3.read() 
	archivo1.close() 
	archivo2.close() 
	archivo3.close() 
	return d1 + d2 + d3 

dt1 = unird("DatosCSC.txt","DatosCSDA.txt","DatosCSDB.txt") 
#dt2 = unird("datos3.txt","datos4.txt","datos5.txt") 



#dt = dt1 + dt2 + dt3
#dat = dt1 + dt2
archivo = open("DatosCSD.txt",'w') 
#archivo.write(dt) 
archivo.write(dt1)
#archivo.write(dt1+dt2+dt3+dt4+dt5)
archivo.close()