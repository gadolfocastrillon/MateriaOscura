
archivo1 = open("AlmacenarDatos/Datos.txt") 
archivo2 = open("datosM2.txt") 
archivo3 = open("AlmacenarDatos/Datos2.txt")


d1 = archivo1.read() 
d2 = archivo2.read() 
d3 = archivo3.read()

dt = d1+d2 +d3


archivo1.close() 
archivo2.close() 
archivo3.close()


archivo = open("Datos.txt",'w') 
archivo.write(dt) 
archivo.close()