import subprocess

X = [0.410235241165042,199.7017885254824,498.59987685938177]

def writer(file,dictionary):
	data1=open(file,'w')
	for items in dictionary.items(): 
		data1.write("%s %s\n"%items)
	data1.close()


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

def search(COMMAND): 
	dato = subprocess.getoutput(COMMAND)
	if(len(dato)>0):
		x_ = float(dato)
	else: 
		x_ = -1
	return x_  

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

sigma_v,ot = d_indirecta(X)
print("El valor para sigma_v es: " + str(sigma_v))
for i in ot: 
	print("El valor de un canal es: " + str(i))