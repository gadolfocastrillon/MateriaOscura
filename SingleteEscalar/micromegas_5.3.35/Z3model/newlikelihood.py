import numpy as np 
import subprocess 
from scipy.optimize import differential_evolution 
from scipy.stats import chi2
import matplotlib.pyplot as plt 
import time 

dim = 4
sltns = 0 
min_chi_sq = 0.
alpha = 0.05
critical_chi_sq = chi2.isf(alpha,2)
data_vector = [] 

#Valores de ligadura 
#Corregir para un scan logaritmico. 
'''
lash_min = 1e-4
lash_max = 1
mass_min = 40
mass_max = 1e4
mu_min = 0 
mu_max = 9000
'''
#Corrección logaritmica 
lash_min = -4 #0.0001
lash_max = 0 #1 
mass_min = 1 #10 
mass_max = 4 #10000
mu_min = 0 #1
mu_max = 4 #10000

min_chi_sq = 0.
alpha = 0.05
critical_chi_sq = chi2.isf(alpha,2)

#Valor de la semilla 
seed = 127

# Color style for output sample points
de_pts = "#91bfdb" # Diver scan
rn_pts = "#fc8d59" # Random scan
gd_pts = "#ffffbf" # Grid scan

def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close()


def writer2(x,file):
	data = open(file,'w') 
	#me guarda los datos de masa, lahs, mu3 y cross section
	for i in x: 
		texto = str(i[0]) + " " + str(i[1]) + " " +str(i[2])+ " " + str(i[3]) +"\n"
		data.write(texto)
	data.close()

def samples_inside(x,chi_sq): 
    delta_chi_sq = chi_sq - min_chi_sq
    inside = delta_chi_sq <= critical_chi_sq
    return x[:, inside]

#Me halla la cross section
def csection(): 
	cs = 0.0
	COMMAND = "grep 'proton  SI' temporal.dat | awk '{print $3}'"
	dato = subprocess.getoutput(COMMAND)
	if(len(dato)>0):
		cs = float(dato)
	else: 
		cs = -1 
	return cs

def omega(X):
	#---------------- Rutas de los archivos -------------------------------
	ruta = 'data.dat' #Ruta para guardar el archivo.
	rutaG = './main data.dat > temporal.dat' #Ruta para ejecutar micromegas 
	#----------------------------------------------------------------------
	
	#------Diccionario con los datos del archivo. -------------------------
	data = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} 
	#Sin correción logaritmica 
	'''
	data['Mp1'] = X[1] #Valores de la masa de la particulas. masa logaritmica. 
	data['laSH1'] = X[0] #Valores de laSH
	data['mu32'] = X[2] #Valores de mu3
	'''
	#Con corrección logaritmica.
	data['Mp1'] = 10**X[1] #Valores de la masa de la particulas. masa logaritmica. 
	data['laSH1'] =10**X[0] #Valores de laSH
	data['mu32'] = 10**X[2] #Valores de mu3
	#print(data)
	#----------------------------------------------------------------------

	#--------------------Sistema de escritura en el archivo----------------
	writer(ruta,data) 
	#----------------------------------------------------------------------

	#--------------------Obtener el valor de la densidad reliquia --------
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
		'''
		if ((omeg <0.130)and(omeg>0.110)):
			cs = csection()
			#Me guarda los puntos de interes para el problema fisico
			data_vector.append([omeg,X[1],X[2],X[3],cs]) 
			sltns+=1
		'''
	else: 
		omeg = -1 
	return omeg
	#----------------------------------------------------------------------

#-------------------------Función gaussiana definida en el articulo --------

def gaussian(X):
	x = omega(X)
	#print(X)
	sigma = np.sqrt((0.1*x)**2 + (0.001)**2) #Defino el sigma 
	xobs = 0.120 #densidad reliquia observable
	return ((x-xobs)/sigma)**2 #Gaussiana

#---------------------------------------------------------------------------

#------------------- Método para differential evolution --------------------
def de_scan(dim,round_to_nearest=None): 
	x = [] 
	chi_sq = []
	cs =[] 
	#lambdaSH, Masa, Mu3
	bounds = [(lash_min,lash_max),(mass_min,mass_max),(mu_min,mu_max)] #ligaduras
	def objective(x_):
		chi_sq_ = gaussian(x_)
		chi_sq.append(chi_sq_)
		x_[0] = 10**x_[0]
		x_[1] = 10**x_[1]
		x_[2] = 10**x_[2]
		x.append(x_)
		cross = csection()
		cs.append(cross)
		#print(x_,cross)
		if (len(x) % 1000 == 0):
			print(len(x))
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
	
	differential_evolution(objective, bounds,
                           strategy='currenttobest1bin', maxiter=None,
                           popsize=200, tol=0.01, mutation=(1.5, 1.99999), recombination=0.9,
                           polish=False, seed=seed)

	#rand1bin, 50, 0.01, 1.5-1.99, 0.9 seed = 10 guardado en 5 
	#currenttobest1exp, 50, 0.01, 1.5-1.99, 0.9 seed = 16 guardado en 12 

	valor = np.array(x).T
	datos=[valor[i] for i in range(len(valor))]
	datos.append(cs) #Agrego cross section a 

	if round_to_nearest is not None: 
		len_x = len(x)
		keep_n = len_x - (len_x %round_to_nearest)
		x = x[:keep_n]
		chi_sq = chi_sq[:keep_n] 

	return samples_inside(np.array(datos),np.array(chi_sq)),len(x)
	#return samples_inside(np.array(x).T, np.array(chi_sq)),len(x)
	#return x
#---------------------------------------------------------------------------
'''
Pendiente: 
Falta guardar los datos, pasar los valores de picmetro² a cm² con 1picometro = 1e-10 cm 
pico² = 1e-20 cm² 
verificar que se guardan los datos del cross section. 

'''
#------------------------------Uso en la función main-----------------------
if __name__ == '__main__':
	#print(seed)
	np.random.seed(seed)
	#print(seed)
	print("Running de_scan")
	
	 
	t0 = time.time()
	x, calls  = de_scan(dim) 	
	#calls me devuelve el tamaño de los datos 
	#x es un arreglo con: x[0]:lambdahs, x[1]: MasaS, x[2]: Mu3, x[3]: cross section.
	writer2(x.T,"datosLikelihood-13.txt") 
	#datosLikelihood-12 de interes
	#datosLikelihood-8 de interes
	#datosLikelihood-9 de interes
	de_time = time.time() - t0 
	print(r'Tiempo de ejecución : '+ str(de_time)) #Imprime el tiempo que demora en ejecutar el progama.
	print("Finalizado")
	'''
	plt.scatter(x[3], x[0], s=30, edgecolor='0.05',
                linewidth=0.25, alpha=1.0, facecolor=de_pts,
                label=r'Differential evolution: \num{{{:d}}} out of \num{{{:d}}} points'
                .format(x.shape[1], calls))
	plt.title("Calculo de la cross section apartir de una likelihood gaussiana") 
	plt.xlabel("Masa") 
	plt.ylabel("Seccion transversal") 
	plt.savefig("Densidad reliquia.svg")
	plt.show()
	'''
	#ax.set_ylabel('Y label',loc='top')
	#ax.set_xlabel('XLabel',loc='left') 
	fig, ax = plt.subplots(figsize=(10,7)) 
	ax.set_xscale('log')
	ax.set_yscale('log')
	im = ax.scatter(x[1],x[3],c=x[2],cmap='viridis')
	fig.colorbar(im)
	plt.title("Singlete escalar con simetría $Z_{3}$")
	plt.ylabel("Cross Section ($\sigma_{SI}$)")
	plt.xlabel("Mass DM (GeV)")
	plt.savefig('mapeo_de_datos_likelihood-9.svg')
	plt.show()
#---------------------------------------------------------------------------