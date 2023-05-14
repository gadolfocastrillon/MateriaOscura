import numpy as np 
import matplotlib.pyplot as plt 

d = np.loadtxt("datosLikelihood.txt") 
print(len(d))

def unird(n):
	dt = ''
	for i in n: 
		archivo = open(i)
		d = archivo.read()
		#print(type(d))
		dt = dt + d 
	#print(dt)
	archivo = open("unionDatos.txt",'w') 
	archivo.write(dt)
	archivo.close() 

def graficador(nombre,guardar="mapeo_de_datos_likelihood.jpg"): 
	datos = np.loadtxt(nombre)
	print("El tamaño de los datos es: "+str(len(datos)))
	fig, ax = plt.subplots(figsize=(10,7)) 
	ax.set_xscale('log')
	ax.set_yscale('log')
	im = ax.scatter(datos.T[1],datos.T[3],c=datos.T[2],cmap='viridis')
	fig.colorbar(im)
	plt.title("Singlete escalar con simetría $Z_{3}$")
	plt.ylabel("Cross Section ($\sigma_{SI}$)")
	plt.xlabel("Mass DM (GeV)")
	plt.savefig(guardar)
	plt.show()

n = ["datosLikelihood.txt","datosLikelihood-1.txt","datosLikelihood-2.txt","datosLikelihood-3.txt","datosLikelihood-4.txt","datosLikelihood-5.txt","datosLikelihood-6.txt"]
unird(n)
graficador('unionDatos.txt')