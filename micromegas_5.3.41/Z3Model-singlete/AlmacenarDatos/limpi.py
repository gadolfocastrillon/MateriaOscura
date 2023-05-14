import numpy as np 
import pandas as pd 

#datos1 = np.loadtxt("datosLikelihood.txt")
datos2 = np.loadtxt("data.txt")

def limpieza(datos):
	df = pd.DataFrame(datos) 
	df = df.drop_duplicates()
	print("Limpiando datos") 
	reof(df)
	return df

def writer(x,file):
	data = open(file,'a') 
	texto = ''
	print("Guardando datos en " + file)
	for i in x:
		texto = str(i[0]) + " " + str(i[1]) + " " +str(i[2])+ " " + str(i[3]) +"\n"
		data.write(texto)
	data.close()

def reof(frame): 
	x1 = frame[0]
	x2 = frame[1]
	x3 = frame[2]
	x4 = frame[3]
	x = []  
	print("Organizando los datos para almacenamiento")
	for i in range(len(x1)): 
		x.append([x1.iloc[i],x2.iloc[i],x3.iloc[i],x4.iloc[i]])	
	writer(x,"dataL2.txt")

limpieza(datos2)
