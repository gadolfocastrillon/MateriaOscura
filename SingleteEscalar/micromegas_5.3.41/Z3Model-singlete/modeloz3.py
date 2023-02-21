import numpy as np 
from numpy import * 
import pandas as pd 
import subprocess 
import sys 
import cmath

newlist1=[]
sltn = 0

def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close() 

def omega(dat): 
	global newlist1,sltns
	writer(ruta,dat) 
	omeg = 0.0 
	#Corriendo micromegas y extrayendo la densidad reliquia 
	subprocess.getoutput(rutaG)
	#aa=subprocess.getoutput("grep 'Omega' temporal.dat")
	#aa2 = subprocess.getoutput("grep 'Omega' temporal.dat")
	#Comando para ejecutar una busqueda desde la terminal 
	#primero grep busca Omega en temporal.dat 
	#Despues awk separa la linea por espacios y me señala la tercer columna 
	COMMAND = "grep 'Omega' temporal.dat | awk 'BEGIN{FS=\"=\"};{print $3}'"  
	dato = subprocess.getoutput(COMMAND) #ejecutar el comando desde la terminal 
	#if ((omegaV>0.0)and(omegaV<0.13)and(omegaV>0.11)): 
	#	print(omegaV)
	if (len(dato)>0): 
		omeg = float(dato) 
	else: 
		omeg = -1 

	if ((omeg<0.13) and (omeg>0.11)):
		sltns+=1 
		newlist1.append([dat['Mh'],dat['laphi'],dat['laSH1'],dat['Mp1'],dat['mu32'],dat['Mtop']])
		return omeg 

dataD = {'Mh':125, 'Mp1':100,'Mp2':300,'Mp3':500,'Mp4':600,'las1':0.1,'las2':0.1,'las3':0.1,'las4':0.1,'las5':0.1,'las6':0.1,'las7':0.1,'mu1':100,'mu2':100,'mu3':100,'mu4':100,'mu5':100}
dataD1 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2}
dataD2 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2}
dataD3 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2}
dataD4 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2}
#ruta = 'micromegas_5.3.41/Z3Model-singlete/data.dat' 
ruta = 'data.dat'
rutaG = './main data.dat > temporal.dat'
datapar={"MH": 125.0, "Mp1": 300, "Mp2": 350, "Mp3": 400, "las1": 0.1, "las2": 0.1, "las3": 0.1, "la412": 0.1, "la413": 0.1, "la423": 0.1, "mus1": 100.0, "mus2": 100.0, "mus3": 100.0, "mus4": 100.0, "la31": 0.01, "la32": 0.01, "la33": 0.01, "la34": 0.01, "la35": 0.01, "la36": 0.01}
sltns=0
#Mh masa de higgs 
#laphi (lambda phi) termino de autointeracción
#laSH (lambda SH) termino de interacción higg particula
#Mp1 masa de la particula phi 
#mu3 parametro nuevo de Z3 
#La idea es variar mu3, laSH y Mp1 y determinar y guardar la info cuando omega = 0.12 con error del 10% 
for irun in range(0,8001,1): 
	if(irun%100==0): 
		print('irun=',irun)
	omega1 = 0.0 
	omega2 = 0.0 
	omega3 = 0.0
	omega4 = 0.0 
	Mp1 = np.random.uniform(10,100) 
	Mp2 = np.random.uniform(1.01,1.3)*Mp1
	Mp3 = np.random.uniform(1.01*Mp2,0.99*(Mp1+Mp2))
	Mp4 = np.random.uniform(1.01,1.3)*Mp3
	las1 = 10**( (log10(5e-2)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
	las2 = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
	las3 = 10**( (log10(1e0)-log10(1e-2))*np.random.uniform(0,1)+log10(1e-2))*(-1)**np.random.randint(0,2)
	las4 = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
	mu1 = np.random.uniform(1000,10000)
	mu2 = np.random.uniform(1000,10000)
	mu3 = np.random.uniform(1000,10000)
	mu4 = np.random.uniform(1000,10000)
	
	#Almacenando los valores creados en un diccionario para guardar
	#Valores de la masa de la particula 
	dataD1['Mp1'] = Mp1 
	dataD2['Mp1'] = Mp2 
	dataD3['Mp1'] = Mp3
	dataD4['Mp1'] = Mp4
	#Valores de laSH 
	dataD1['laSH1'] = las1
	dataD2['laSH1'] = las2
	dataD3['laSH1'] = las3
	dataD4['laSH1'] = las4
	#Valores de mu3
	dataD1['mu32'] = mu1
	dataD2['mu32'] = mu2
	dataD3['mu32'] = mu3
	dataD4['mu32'] = mu4
		
	omega1 = omega(dataD1) 
	omega2 = omega(dataD2) 
	omega3 = omega(dataD3) 
	omega4 = omega(dataD4) 

print('sltns=',sltns)
datos = np.asarray(newlist1)
np.savetxt('datos10-100.txt',datos)