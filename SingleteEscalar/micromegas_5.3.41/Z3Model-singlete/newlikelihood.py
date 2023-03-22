import numpy as np 
import subprocess 
from scipy.optimize import differential_evolution 
import matplotlib.pyplot as plt 
import time 
dim = 3
sltns = 0 
def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close()

def samples_inside(x,chi_sq): 
    delta_chi_sq = chi_sq - min_chi_sq
    inside = delta_chi_sq <= critical_chi_sq
    return x[:, inside]

def omega(X):
	m = X[0]
	lam = X[1]
	u3 = X[2]
	#---------------- Rutas de los archivos -------------------------------
	ruta = 'data.dat' #Ruta para guardar el archivo.
	rutaG = './main data.dat > temporal.dat' #Ruta para ejecutar micromegas 
	#----------------------------------------------------------------------
	
	#------Diccionario con los datos del archivo. -------------------------
	data = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} 
	data['Mp1'] = m #Valores de la masa de la particulas.
	data['laSH1'] = lam #Valores de laSH
	data['mu32'] = u3 #Valores de mu3
	#----------------------------------------------------------------------

	#--------------------Sistema de escritura en el archivo----------------
	writer(ruta,data) 
	#----------------------------------------------------------------------

	#--------------------Obtener el valor de la densiadad reliquia --------
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
	#----------------------------------------------------------------------

	return omeg #Retorna el valor de la densidad reliquia.

#-------------------------Función gaussiana definida en el articulo --------

def gaussian(X):
	x = omega(X)
	sigma = ((0.1*x)**2 + (0.001)**2)**(0.5) #Defino el sigma 
	xobs = 0.120 #densidad reliquia observable
	return (x-xobs)/sigma  
#---------------------------------------------------------------------------

#------------------- Método para differential evolution --------------------
def de_scan(dim,round_to_nearest=None): 
	x = [] 
	chi_sq = [] 
	bounds = [(0,1000),(1e-4,1e-2),(0,5000)] #ligaduras

	def objective(x_): 
		chi_sq_ = gaussian(x_)
		chi_sq.append(chi_sq_)
		x.append(x_)
		return chi_sq_
	#strategy condiciones a cumplir la estrategia 
	#popsize cantidad de individuos cantidatos a generar 
	#tol tolerancia del problema? error del problema? 
	#mutation capacidad de mutación de los datos al partir de 2 padres y crear un hijo 
	#La mutación esta entre un minimo y un maximo de mutación (min,max)
	#recombination es conocida como probabilidad de cruce. 
	#El aumento de este valor permite que una mayor cantidad de mutates progresen a la siguiente generación
	#pero a riegos de la estabilidad de la población.
	#Especificar seed para minimizaciones repetibles.
	#Polish se usa para pulir el mejor miembro de la población final, mejora ligeramente la minimización.
	#Para problemas grandes con muchas restricciones, el pulido puede llevar mucho tiempo debido a los calculos jacobianos.
	differential_evolution(gaussian, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=10)
	'''
	datos = differential_evolution(gaussian, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=10)
	'''

	if round_to_nearest is not None: 
		len_x = len(x)
		keep_n = len_x - (len_x %round_to_nearest)
		x = x[:keep_n]
		chi_sq = chi_sq[:keep_n] 

	#print(np.array(x))
	return samples_inside(np.array(x).T, np.array(chi_sq)),len(x)
	'''
	print(datos.x)
	data2=open("informacion.txt",'w')
	data2.write(datos.x)
	#data2.close()
	return datos
	'''
#---------------------------------------------------------------------------

#------------------------------Uso en la función main-----------------------
if __name__ == '__main__': 
	#np.random.seed(seed) 
	plt.figure(figsize=(10,7))
	print("Running de_scan") 
	t0 = time.time()
	#x, calls = de_scan(dim,round_to_nearest=1000) 
	x = de_scan(dim,round_to_nearest=1000) 
	de_time = time.time() - t0 
	print("Plotting de_scan") 
	print(r'Tiempo de ejecución : '+ str(de_time)) #Imprime el tiempo que demora en ejecutar el progama.
	print(x)
#---------------------------------------------------------------------------