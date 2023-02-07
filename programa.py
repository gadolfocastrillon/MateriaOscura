import numpy as np 
import os 

archivo = open('datos.txt','w')
archivo.close()


#os.system('make main=main.c')
#os.system('clear')
'''
Funcion editar: 
-Ingresa 
	Mdm1: Masa de la materia oscura.
	laSH : Parametro de interacción de la materia oscura consigo misma. 
Este modifica el archivo de texto de data2.par, cambiando los parametros de Mdm1 y laS 
te devuelve un vector llamado datos con la información del archivo de texto modificado. 
'''
def editar(Mdm1,laSH): 
	datos = []
	for linea in open("data2.par"): 
		datos.append(linea)
	datos[3] = 'laSH'+'   '+str(laSH)+'\n'
	datos[4] = 'Mdm1' + '   '+ str(Mdm1)+'\n'
	return datos


'''
Funcion escribir: 
-Le ingresas un archivo de datos como el generado por editar y el se encarga de almacenarlo 
en el archivo datos2.par con la misma sintasis.  
'''
def escribir(datos): 
	archivo=open("data2.par",'w')
	for i in datos: 
		archivo.write(i)
	archivo.close()


def analisis(Mdm1,laSH): 
	import re 
	datos = [] 
	for linea in open('temporal.dat'): 
		datos.append(linea)
	
	archivo = open('datos.txt','a')
	#texto = str(Mdm1) + '	' +str(laSH)+ '	' +str(float(datos[9].split('=')[2]))+'\n'
	#archivo.write(texto)
	
	val = float(datos[9].split('=')[2])
	if((val<=0.132)&(val>=0.108)): 
		archivo.write(str(Mdm1) + '	' +str(laSH)+ '	' +str(val)+'\n')
		datos = []
	archivo.close()


for i in range(10,100,1):
	for j in np.arange(0.01,1,0.01):
		datos = editar(i,j)
		escribir(datos)
		os.system('./main data2.par>temporal.dat')
		analisis(i,j)


