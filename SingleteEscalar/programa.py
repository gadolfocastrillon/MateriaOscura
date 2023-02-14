import numpy as np 
import os 
import pandas as pd 
ruta = 'micromegas_5.3.41/SingletDM/data2.par'

rutaG = '''cd micromegas_5.3.41/SingletDM/\n
./main data2.par > ~/Escritorio/trabajo_de_grado/MateriaOscura/SingleteEscalar/temporal.dat
'''
elimin = '\n==== Calculation of relic density ====='
elimin2 = '''\n==== Calculation of CDM-nucleons amplitudes  ====='''
elimin3 = '\n~x1-nucleon cross sections[pb] ===='
rutaDatos = 'AlmacenarDatos/Datos.csv'
#os.system(rutaG) 

def editar(Mdm1,laSH): 
	#print("ejecutando editar")
	edicion = '''Q      14
Mh     125
laS    0.1
'''
	tex1 = 'laSH   '+ str(laSH)+'\n'
	tex2 = 'Mdm1   '+ str(Mdm1)+'\n'
	global ruta 
	archivo= open(ruta,'w') 
	archivo.write(edicion+tex1+tex2)
	archivo.close()

def temporal(): 
	archivo = open('temporal.dat','r') 
	datos = archivo.read() 
	archivo.close() 
	os.system('rm temporal.dat')
	return datos

def rutina2(ruta):
	
	df = pd.read_csv(ruta)
	#print(df.head())
	'''
	editar(df.iloc[50]['Mass DM'],df.iloc[50]['SSHH'])
	os.system(rutaG)
	
	archivo = temporal() 
	print(archivo)
	datos = archivo.strip(elimin2)

	#val = float(datos[datos.find('proton:  si  '):datos.find('  sd  ')].strip('proton:  si  '))
	valor1 = datos[datos.find('SI'):datos.find('SD')].strip('SI  ')
	valor2 = datos[datos.find('SI',120):datos.find('SD',120)].strip('SI ')
	'''
	

	dat1 = []
	dat2 = [] 
	for i in range(0,len(df)): 
		editar(df.iloc[i]['Mass DM'],df.iloc[i]['SSHH'])
		os.system(rutaG)
		archivo = temporal()
		#print(archivo)
		datos = archivo.strip(elimin2).capitalize()
		#print(datos)
		#print(datos.find('si'))
		valor1 = datos[datos.find('si'):datos.find('sd')].strip('si  ')
		valor2 = datos[datos.find('si',120):datos.find('sd',120)].strip('si ')
		dat1.append(valor1) 
		dat2.append(valor2)
	df['SI 1'] = dat1 
	df['SI 2'] = dat2
	
	df.to_csv('AlmacenarDatos/InteraccionDM-P.csv', header=df.columns,index=False)

rutina2(rutaDatos)


def lya(Mdm1,laSH): 
	
	#Abre el archivo y me almacena los datos
	archivo = open('temporal.dat','r')
	datos = archivo.read()
	archivo.close()
	os.system('rm temporal.dat') #Elimina el archivo temporal.dat

	#Elimina la parte superior de la información
	datosL = datos.strip(elimin).capitalize() 
	datosL = temporal(elimin)
	#Separa el valor respectivo de la densidad reliquia
	val = float(datosL[datosL.find("omega="):datosL.find('\n')].strip("omega="))


	if ((val<=0.132 )&(val>=0.108)): 
		almacenar = str(Mdm1) + '	' +str(laSH)+ '	' +str(val)+'\n'
		archivo = open('datosM2.txt','a') #Abre el archivo para guardar los datos
		print(almacenar)
		archivo.write(almacenar)
		archivo.close()
		return True

'''
generadorMSH genera los valores de masa y laSH que cumplan la condicion ingresada anteriormente
-Minimo y maximo de la masa 
-Minimo y maximo de lambda SH 
-Paso de masa 
-Paso de lambda SH 
'''
def generadorMSH(minM,maxM,minS,maxS,pasoM,pasoS):
	global rutaG 
	for masa in np.arange(minM,maxM,pasoM): 
		for factor in np.arange(minS,maxS,pasoS): 
			editar(masa,factor) 
			os.system(rutaG)
			if(lya(masa,factor)): 
				break


'''
for masa in range(61,200,1):
	for factor in np.arange(1e-4,1e-1,1e-4):
		editar(masa,factor)
		os.system(rutaG)
		if(lya(masa,factor)): 
			break
'''



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
'''
def editar(Mdm1,laSH): 
	datos = []
	global ruta
	for linea in open(ruta):
		datos.append(linea)
	datos[3] = 'laSH'+'   '+str(laSH)+'\n'
	datos[4] = 'Mdm1' + '   '+ str(Mdm1)+'\n'
	return datos
'''
'''
Funcion escribir: 
-Le ingresas un archivo de datos como el generado por editar y el se encarga de almacenarlo 
en el archivo datos2.par con la misma sintasis.  
'''
'''
def escribir(datos): 
	archivo=open(ruta,'w')

	archivo.close()
'''
#datos = editar(100,0.12)
#print(datos)
#escribir(datos)
'''
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
'''

'''
for i in range(10,100,1):
	for j in np.arange(0.01,1,0.01):
		datos = editar(i,j)
		escribir(datos)
		os.system('./main data2.par>temporal.dat')
		analisis(i,j)
'''