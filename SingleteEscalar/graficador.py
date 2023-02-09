import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

ruta = 'AlmacenarDatos/datosM1.txt' 
archivo = open(ruta)

datos = [] 
for linea in archivo: 
	datos.append(linea.split())
	
archivo.close()

df = pd.DataFrame(datos, columns=['DM Mass','SSHH', 'Omega'])
print(df.pivot(index='SSHH',columns=))
