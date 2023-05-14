import numpy as np 
import pandas as pd 

datos = np.loadtxt("AlmacenarDatos/unionDatos70-1000.txt")

print(len(datos))
def escritura(X):
	texto = "" 
	for te in X: 
		texto += str(te) + " "
	texto += "\n"
	return texto 
archivo = open("otrosDatos.txt",'w') 

for i in range(28261,len(datos)):
	archivo.write(escritura(datos[i]))
archivo.close()
#df = pd.DataFrame(datos)
#print(df)
#print(df[100])
