
archivo1 = open("Datos1.txt") 
archivo2 = open("datos2000-3000.txt") 
#archivo3 = open("datos1000-2000.txt")


d1 = archivo1.read() 
d2 = archivo2.read() 
#d3 = archivo3.read()

#dt = d1+d2 +d3
dt = d1+d2 

archivo1.close() 
archivo2.close() 
#archivo3.close()


archivo = open("Datos.txt",'w') 
archivo.write(dt) 
archivo.close()