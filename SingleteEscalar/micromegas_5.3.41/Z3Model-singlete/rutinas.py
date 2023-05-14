import numpy as np 
import subprocess 
from scipy.optimize import differential_evolution 
from scipy.stats import chi2
import matplotlib.pyplot as plt 
import time 

dim = 4
sltns = 0 
data_vector = [] 

#Valores de ligadura 
lash_min = 1e-4
lash_max = 1.0
mass_min = 1e1 
mass_max = 1e3
mu_min = 0
mu_max = 1e4

#Valores para chi_cuadrado
min_chi_sq = 0.
alpha = 0.05
critical_chi_sq = chi2.isf(alpha,2)

#Se encarga de escribir el diccionario en un archivo que se le pasa. 
def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close()

#ejecuta una serie de comando para ejecutar micromegas
def ejecutable(X): 
	#---------------- Rutas de los archivos -------------------------------
	ruta = 'data.dat' #Ruta para guardar el archivo.
	rutaG = './main data.dat > temporal.dat' #Ruta para ejecutar micromegas 
	#----------------------------------------------------------------------
	
	#------Diccionario con los datos del archivo. -------------------------
	data = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} 
	data['Mp1'] = X[1] #Valores de la masa de la particulas.
	data['laSH1'] = X[0] #Valores de laSH
	data['mu32'] = X[2] #Valores de mu3
	#print(data)
	#----------------------------------------------------------------------

	#--------------------Sistema de escritura en el archivo----------------
	writer(ruta,data) 
	#----------------------------------------------------------------------

	#--------------------Obtener el valor de la densidad reliquia --------
	omeg = 0.0 
	#Corriendo micromegas y extrayendo la densidad reliquia 
	subprocess.getoutput(rutaG)

#Le paso el comando y me busca el dato a obtener, retorna el dato obtenido, solo valores numericos
def search(COMMAND): 
	dato = subprocess.getoutput(COMMAND)
	if(len(dato)>0):
		x_ = float(dato)
	else: 
		x_ = -1
	return x_  

#Me halla la densidad reliquia
def omega(X):
	ejecutable(X) 
	COMMAND = "grep 'Omega' temporal.dat | awk 'BEGIN{FS=\"=\"};{print $3}'"  
	return search(COMMAND)

def csection(): 
	return search("grep 'proton  SI' temporal.dat | awk '{print $3}'")

def csection_ejecutable(X): 
	ejecutable(X)
	COMMAND = "grep 'proton  SI' temporal.dat | awk '{print $3}'"
	return search(COMMAND)

#Me halla la sigmaV y los valores de los diferentes canales 
def d_indirecta(X): 
	ejecutable(X)
	dicc = ["'~phi1,~phi1 -> h ~PH'","'~phi1,~PHI1 -> W+ W-'","'~phi1,~PHI1 -> Z Z'","'~phi1,~PHI1 -> t T'","'~phi1,~PHI1 -> h h'"]
	dat = [] 
	COMMAND_SV = "grep 'annihilation cross section' temporal.dat | awk '{print $4}'"
	sigma_v = search(COMMAND_SV)
	n = int(len(dicc))
	for i in dicc: 
		COMMAND = "grep " + i + " temporal.dat | awk '{print $5}'"
		obt = search(COMMAND)
		dat.append(obt)
	return sigma_v,dat

#Uso de una función de probabilidad Gaussiana para hallar la densidad reliquia.
def gaussian(X):
	x = omega(X)
	sigma = np.sqrt((0.1*x)**2 + (0.001)**2) #Defino el sigma 
	xobs = 0.120 #densidad reliquia observable
	return ((x-xobs)/sigma)**2 #Gaussiana

#Apartir de un valor minimo de chi, me separa los datos entre los que son validos y los que no.
def samples_inside(x,chi_sq): 
    delta_chi_sq = chi_sq - min_chi_sq
    inside = delta_chi_sq <= critical_chi_sq
    return x[:, inside]

#de_scan usa el algoritmo de differential evolution para calcular valores de densidad reliquia
def de_scan(dim,round_to_nearest=None): 
	x = [] 
	chi_sq = []
	cs =[] 
	#lambdaSH, Masa, Mu3
	bounds = [(lash_min,lash_max),(mass_min,mass_max),(mu_min,mu_max)] #ligaduras
	def objective(x_):
		chi_sq_ = gaussian(x_)
		chi_sq.append(chi_sq_)
		x.append(x_)
		cross = csection()
		cs.append(cross)
		#print(x_,cross)
		if (len(x) % 10000 == 0):
			print(len(x))
		return chi_sq_

	differential_evolution(objective, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=100, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=120)
	
	valor = np.array(x).T
	datos=[valor[i] for i in range(len(valor))]
	datos.append(cs) #Agrego cross section a 

	if round_to_nearest is not None: 
		len_x = len(x)
		keep_n = len_x - (len_x %round_to_nearest)
		x = x[:keep_n]
		chi_sq = chi_sq[:keep_n] 

	return samples_inside(np.array(datos),np.array(chi_sq)),len(x)