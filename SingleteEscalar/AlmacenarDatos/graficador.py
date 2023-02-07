import numpy as np 
import matplotlib.pyplot as plt 

archivo = open('datos.txt') 
x=[]
y=[]
for linea in archivo: 
	datos = linea.split()
	x.append(datos[0])
	y.append(datos[1])



archivo.close() 
plt.figure()
plt.plot(x,y,'-o') 
plt.ylim(0,10)
plt.grid()
plt.show()





