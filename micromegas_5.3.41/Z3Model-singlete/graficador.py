import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

nombre = 'datosSigma.txt'
datos = np.loadtxt(nombre)
#print(datos.T[3])
def graficarCs(datos):
	df = pd.DataFrame(datos,columns=['MH','laphi','laSH','Mp','mu3','cs'])
	fig, ax = plt.subplots(figsize=(9,7)) 
	ax.set_xscale('log')
	ax.set_yscale('log')
	im = ax.scatter(df['Mp'],df['cs'],c=df['mu3'],cmap='viridis')
	fig.colorbar(im)
	#plt.xlim(0,1000)
	plt.title("Singlete escalar con simetría $Z_{3}$")
	plt.ylabel("Cross Section ($\sigma_{SI}$)")
	plt.xlabel("Mass DM (GeV)")
	plt.savefig('AlmacenarDatos/mapeo_de_datos.svg')
	plt.show()

def graficarID(datos): 
	cross_section = datos.T[3]
	chanells_DmH = datos.T[4] 
	mass = datos.T[1]
	sigma_v = cross_section*chanells_DmH
	#print(y)
	plt.figure() 
	plt.plot(mass,cross_section,'.')
	plt.xlabel("$m_DM$  (GeV)")
	plt.ylabel("$<\sigma v>$ ($cm^{3}s^{-1}$)")
	plt.show()

graficarID(datos)

