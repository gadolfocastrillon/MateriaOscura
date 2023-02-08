import numpy as np 
import matplotlib.pyplot as plt 

ruta = 'AlmacenarDatos/datosM1.txt'
X = [] 
Y = [] 
archivo = open(ruta)
for linea in archivo: 
	arc = linea.split()
	X.append(arc[0])
	Y.append(arc[1])

plt.figure(figsize=(10,10))
plt.plot(X,Y,'.') 
plt.show()