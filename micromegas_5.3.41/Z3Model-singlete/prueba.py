import numpy as np 
import subprocess 
import time 
from scipy.optimize import differential_evolution

nombre = 'AlmacenarDatos/DatosLikelihood.txt'
datos = np.loadtxt(nombre) 
print("El tamaño de los datos es " +str(len(datos)))

for dat in datos:
	print(dat)

dic = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2}

def ejecutar(linea): 
	dic['laSH1'] = linea[0]
	dic['Mp1'] = linea[1]
	dic['mu32'] = linea[2]





'''
x = [] 
chi_sq = [] 
data = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} #Diccionario con los datos del archivo.
ruta = 'data.dat' #Ruta para guardar el archivo.
rutaG = './main data.dat > temporal.dat' #Ruta para ejecutar micromegas 
sltns=0 #Numero de datos guardados. 


def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close()

def omega(m,lam,u3):
	data = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} #Diccionario con los datos del archivo.
	data['Mp1'] = m #Valores de la masa de la particulas.
	data['laSH1'] = lam #Valores de laSH
	data['mu32'] = u3 #Valores de mu3
	writer(ruta,data) 
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

	return omeg

def funcion(x): 
	sigma = ((0.1*x)**2 + (0.001)**2)**(0.5) #Defino el sigma 
	xobs = 0.120 #densidad reliquia observable
	return (x-xobs)/sigma 

for i in range(0,100): 
	#print(funcion(omega(i,0,0)))
	print(omega(i,1e-2,0))
'''
'''
def objective(x_): 
		chi_sq_ =funcion(x_) 
		chi_sq.append(chi_sq_) 
		x.append(x_) 
		return chi_sq_

differential_evolution(objective, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=seed)

print(x[0])
'''
'''
newlist1=[] #Arreglo para guardar los valores que necesitamos. 
dicc = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} #Diccionario con los datos del archivo.
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
	dicc['Mp1'] = X[0] #Valores de la masa de la particulas.
	dicc['laSH1'] = X[1] #Valores de laSH
	dicc['mu32'] = X[2] #Valores de mu3
	writer(ruta,dicc) 
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
		newlist1.append([dicc['Mh'],dicc['laphi'],dicc['laSH1'],dicc['Mp1'],dicc['mu32'],dicc['Mtop']])

	return omeg

for irun in range(0,1000,1): 
	if(irun%100==0): 
		print('irun='+str(irun) + ' time='+str(time.process_time()))
		print(sltns)
	Mp1 = np.random.uniform(100,200) 
	#las1 = 10**( (log10(5e-2)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
	las1 = np.random.uniform(1e-4,1e-2)
	mu1 = np.random.uniform(0,4000)
	X = [Mp1,las1,mu1]
	omega(X)

print('sltns=',sltns)
'''