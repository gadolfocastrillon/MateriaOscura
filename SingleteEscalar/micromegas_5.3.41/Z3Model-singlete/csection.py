import numpy as np
import subprocess 
import sys

def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close() 

ruta = 'data.dat'
rutaG = './main data.dat > temporal.dat'
nombre = 'dataL2.txt'
datos = np.loadtxt(nombre) 
dic = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2}
dic2 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'cross_section':0.0}
newlist = []
def ejecutar(linea):
	dic['Mp1'] = linea[1]
	dic['laSH1'] = linea[2]
	dic['mu32'] = linea[3]
	writer(ruta,dic)
	subprocess.getoutput(rutaG)
	COMMAND = "grep 'proton  SI' temporal.dat | awk '{print $3}'"
	dato = subprocess.getoutput(COMMAND)
	dic2['Mp1'] = linea[1]
	dic2['laSH1'] = linea[2]
	dic2['mu32'] = linea[3]
	if(len(dato)>0): 
		dic2['cross_section'] = float(dato)
		#print(float(dato))
	else: 
		dic2['cross_section'] = -1
	#newlist.append([dic2['Mh'],dic2['laphi'],dic2['laSH1'],dic2['Mp1'],dic2['mu32'],dic2['cross_section']]) 
	newlist.append([dic2['Mp1'],dic2['laSH1'],dic2['mu32'],dic2['cross_section']])

irun = 0 
print("El tamaño de los datos es " +str(len(datos)))
for linea in datos: 
	if(irun%1000==0): 
		print('irun=',irun)
	ejecutar(linea)
	irun+=1

datos = np.asarray(newlist)
np.savetxt('datosLikelihoodP8.txt',datos)
