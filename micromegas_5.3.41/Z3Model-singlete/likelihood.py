import numpy as np 
import subprocess
from scipy.optimize import differential_evolution
from scipy.stats import chi2
import matplotlib.pyplot as plt 
import time 

newlist1=[] #Arreglo para guardar los valores que necesitamos. 
dataD1 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} #Diccionario con los datos del archivo.
ruta = 'data.dat' #Ruta para guardar el archivo.
rutaG = './main data.dat > temporal.dat' #Ruta para ejecutar micromegas 
sltns=0 #Numero de datos guardados. 

xobs =[]
#Las ligaduras se usan para establecer valores minimos y maximos entre los cuales queremos
#aplicar differential_evolution.
min_masa = 0 #Valor minimo de la masa 
max_masa = 1000 #Valor maximo de la masa 
min_lambda = 1e-4 #Valor minimo de lambdahs
max_lambda = 1e-2 #Valor maximo de lambdahs
min_mu3 = 0 #Valor minimo de mu3 
max_mu3 = 1000 #Valor maximo de mu3 
dim = 3 #
bounds=[(min_masa,max_masa),(min_lambda,max_lambda),(min_mu3,max_mu3)] #Creo 4 ligaduras. 
seed = 120 
min_chi_sq = 0.
alpha = 0.05
critical_chi_sq = chi2.isf(alpha,2)

# Color style for output sample points
de_pts = "#91bfdb" # Diver scan
rn_pts = "#fc8d59" # Random scan
gd_pts = "#ffffbf" # Grid scan

def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	print(data1)
	data1.close() 

def omega(m,lam,u3):
	global newlist1,sltns, dataD1
	dataD1['Mp1'] = m #Valores de la masa de la particulas.
	dataD1['laSH1'] = lam #Valores de laSH
	dataD1['mu32'] = u3 #Valores de mu3
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

	return omeg

def samples_inside(x,chi_sq): 
    delta_chi_sq = chi_sq - min_chi_sq
    inside = delta_chi_sq <= critical_chi_sq
    return x[:, inside]

def gaussian(x):
	sigma = ((0.1*x)**2 + (0.001)**2)**(0.5) #Defino el sigma 
	xobs = 0.120 #densidad reliquia observable
	return (x-xobs)/sigma 


def gaussian_general(x): 
	n = len(x) 
	#Creo la suma de las gaussianas. 
	#llamando a la funcion de arriba gaussian
	return sum((gaussian(x[i])**2) for i in range(n-1)) 


def de_scan(dim,round_to_nearest=None): 
	x = [] 
	chi_sq = [] 

	#Función objetivo para minimizar con differential_evolution
	def objective(omega): 
		chi_sq_ = gaussian_general(func)
		chi_sq.append(chi_sq_) 
		x.append(x_) 
		return chi_sq_

	differential_evolution(objective, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=seed)

	if round_to_nearest is not None: 
		len_x = len(x)
		keep_n = len_x - (len_x %round_to_nearest)
		x = x[:keep_n]
		chi_sq = chi_sq[:keep_n] 
	#print(np.array(x))
	return samples_inside(np.array(x).T, np.array(chi_sq)),len(x)


if __name__ == '__main__': 
	np.random.seed(seed) 
	plt.figure(figsize=(10,7))
	print("Running de_scan") 
	t0 = time.time()
	x, calls = de_scan(dim,round_to_nearest=1000) 
	de_time = time.time() - t0 
	print("Plotting de_scan") 
	print(r'Tiempo de ejecución : '+ str(de_time)) #Imprime el tiempo que demora en ejecutar el progama.
	print(x)
	'''
	plt.scatter(x[0], x[1], s=30, edgecolor='0.05',
                linewidth=0.25, alpha=1.0, facecolor=de_pts,
                label=r'Differential evolution: \num{{{:d}}} out of \num{{{:d}}} points'
                .format(x.shape[1], calls))
	plt.title("Funcion Gaussiana para la densidad reliquia") 
	plt.xlabel("Parametro densidad reliquia 1") 
	plt.ylabel("Prametro densidad reliquia 2") 
	plt.savefig("Densidad reliquia.svg")
	plt.show()
	'''