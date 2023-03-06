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

dt1 = unird("DatosCSB1.txt","DatosCSB2.txt","DatosCSA.txt") 
#dt2 = unird("datos5.txt","datos3.txt","datos4.txt") 
#dt3 = unird("datos7.txt","datos8.txt","datos9.txt")

#dt = dt1 + dt2 + dt3
#dat = dt1 + dt2
archivo = open("DatosCSB.txt",'w') 
#archivo.write(dt) 
archivo.write(dt1)
archivo.close()