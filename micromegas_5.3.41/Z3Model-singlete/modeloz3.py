import numpy as np
from numpy import * 
import subprocess 
import matplotlib.pyplot as plt
import time
#Mh masa de higgs 
#laphi (lambda phi) termino de autointeracción
#laSH (lambda SH) termino de interacción higg particula
#Mp1 masa de la particula phi 
#mu3 parametro nuevo de Z3 
#La idea es variar mu3, laSH y Mp1 y determinar y guardar la info cuando omega = 0.12 con error del 10% 


newlist1=[] #Arreglo para guardar los valores que necesitamos. 
dataD1 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} #Diccionario con los datos del archivo.
ruta = 'data.dat' #Ruta para guardar el archivo.
rutaG = './main data.dat > temporal.dat' #Ruta para ejecutar micromegas 
sltns=0 #Numero de datos guardados. 

def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close() 

def omega(X): 
	global newlist1,sltns,dataD1
	dataD1['Mp1'] = X[0] #Valores de la masa de la particulas.
	dataD1['laSH1'] = X[1] #Valores de laSH
	dataD1['mu32'] = X[2] #Valores de mu3
	writer(ruta,dataD1) 
	omeg = 0.0 
	#Corriendo micromegas y extrayendo la densidad reliquia 
	subprocess.getoutput(rutaG)
	#Comando para ejecutar una busqueda desde la terminal 
	#primero grep busca Omega en temporal.dat 
	#Despues awk separa la linea por espacios y me señala la tercer columna 
	COMMAND = "grep 'Omega' temporal.dat | awk 'BEGIN{FS=\"=\"};{print $3}'"  
	dato = subprocess.getoutput(COMMAND) #ejecutar el comando desde la terminal 
	if (len(dato)>0): 
		omeg = float(dato) 
	else: 
		omeg = -1 

	if ((omeg<0.13) and (omeg>0.11)):
		sltns+=1 
		newlist1.append([dat['Mh'],dat['laphi'],dat['laSH1'],dat['Mp1'],dat['mu32'],dat['Mtop']])

	return omeg
	

for irun in range(0,20000,1): 
	if(irun%100==0): 
		print('irun='+str(irun) + ' time='+str(time.process_time()))
		print(sltns)
	#Variación de los parametros.
	Mp1 = np.random.uniform(100,200) 
	#las1 = 10**( (log10(5e-2)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
	las1 = np.random.uniform(1e-4,1e-2)
	mu1 = np.random.uniform(0,4000)

	dataD1['Mp1'] = Mp1  #Valores de la masa de la particulas.
	dataD1['laSH1'] = las1 #Valores de laSH
	dataD1['mu32'] = mu1 #Valores de mu3
	
	omega(dataD1)  #Llamo a la rutina omega que me comprueba el valor de la densidad reliquia
	

print('sltns=',sltns)
datos = np.asarray(newlist1)
np.savetxt('AlmacenarDatos/datos8.txt',datos)
'''
plt.figure(figsize=(9,7)) 
plt.plot(datos[4],datos[3],'k.')
plt.show()
'''