import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#Nombre de los archivos
nombre1 = 'datosSigma.txt'
nombre2 = 'datosSigma2.txt'
nombre_CMB='Datos-experimentales-modelo-Z3/CMB.dat'
nombre_CTA='Datos-experimentales-modelo-Z3/CTA.dat'
nombre_Fermi='Datos-experimentales-modelo-Z3/Fermi-LAT.dat'
nombre_Mess='Datos-experimentales-modelo-Z3/MESS-GC.dat'
#Cargado de los datos del programa.
datos1 = np.loadtxt(nombre1)
datos2 = np.loadtxt(nombre2)

mass1 = datos1.T[1] #Datos de masa 
sigma_v1 = datos1.T[3]*datos1.T[4]  #Hallo el procentaje de sigma_v
mass2 = datos2.T[1] #Datos de masas 
sigma_v2 = datos2.T[3]*datos2.T[4] 
sigma = [] 
mass = [] 
#Organizar datos en un arreglo todos. 
for i in range(len(mass1)): 
	mass.append(mass1[i])
	sigma.append(sigma_v1[i])
for i in range(len(mass2)): 
	mass.append(mass2[i])
	sigma.append(sigma_v2[i])


datos_CMB = np.loadtxt(nombre_CMB) #Cargo los datos del CMB 
datos_CTA = np.loadtxt(nombre_CTA) #Cargo los datos del CTA 
datos_Fermi = np.loadtxt(nombre_Fermi) #Cargo los datos del Fermi-LAT
datos_Mess = np.loadtxt(nombre_Mess) #Cargo los datos del HESS
#print(datos_CMB.T)

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
#print(len(datos2.T))


plt.figure() 
plt.plot(mass,sigma,'m.',label="Simulación del modelo Z3")
plt.plot(datos_CMB.T[0],datos_CMB.T[1],'k',label="CMB")
plt.plot(datos_CTA.T[0],datos_CTA.T[1],'b',label="CTA (prospects)")
plt.plot(datos_Fermi.T[0],datos_Fermi.T[1],'g',label="Fermi-LAT-dSph")
plt.plot(datos_Mess.T[0],datos_Mess.T[1],'c',label="HESS-GC")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$m_DM$  (GeV)")
plt.legend()
plt.ylabel("$<\sigma v>$	 ($cm^{3}s^{-1}$)")
plt.savefig("Resultados de detección indirecta.jpg")
plt.show()

#graficarID(datos1,datos2,datos_experimentales)
#print(datos_experimentales.T)

