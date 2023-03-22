import numpy as np 
import matplotlib.pyplot as plt 
import time 


class Modelo: 
	def __init__(self,dictionary): 
		self.dictionary = dictionary
		self.dictionay2 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'cross_section':0.0}
		self.ruta = 'data.dat'
		self.rutaG = './main data.dat > temporal.dat'
		self.sltns = 0
		self.newlist1 = []
		self.newlist2 = []
		self.datos = 'Datos.txt' 
		

	def setruta(self,direccion): 
		self.file = direccion
	def getruta(self):
		return self.file 
	def setRutaG(self,direccion): 
		self.rutaG = direccion
	def getRutaG(self):
		return self.rutaG 
	def setCargado(self,direccion): 
		self.datos = direccion 
	def setDatos(self,direccion): 
		self.datos = direccion
	def getDatos(self): 
		return self.datos 

	def writer(self):
		data1=open(self.ruta,'w')
		for items in self.dictionary.items(): 
			data1.write("%s %s\n"%items)
		data1.close() 

	def omega(self,dat): 
		writer() 
		omeg = 0.0 
		subprocess.getoutput(self.rutaG) 
		COMMAND = "grep 'Omega' temporal.dat | awk 'BEGIN{FS=\"=\"};{print $3}'"  
		dato = subprocess.getoutput(COMMAND) #ejecutar el comando desde la terminal 
		if (len(dato)>0): 
			omeg = float(dato) 
		else: 
			omeg = -1
		if((omeg<0.13) and (omeg>0.11)): 
			self.sltns+=1 
			self.newlist1.append([dat['Mh'],dat['laphi'],dat['laSH1'],dat['Mp1'],dat['mu32'],dat['Mtop']])
		
	def unird(n1,n2,n3=''): 
		archivo1 = open(n1) 
		archivo2 = open(n2) 
		d1 = archivo1.read()
		d2 = archivo2.read() 
		try: 
			archivo3 = open(n3) 
			d3 = archivo3.read()
			archivo1.close() 
			archivo2.close() 
			archivo3.close() 
			return d1 + d2 + d3 
		except TypeError: 
			archivo1.close() 
			archivo2.close()
			return d1 + d2 	

	def cseccion(self,linea): 
		self.dictionary['laSH1'] = linea[2]
		self.dictionary['Mp1'] = linea[3]
		self.dictionary['mu32'] = linea[4]
		writer() 
		subprocess.getoutput(self.rutaG) 
		COMMAND = "grep 'proton  SI' temporal.dat | awk '{print $3}'"
		dato = subprocess.getoutput(COMMAND)
		self.dictionary2['laSH1'] = linea[2]
		self.dictionary2['Mp1'] = linea[3]
		self.dictionary2['mu32'] = linea[4]
		if(len(dato)>0): 
			self.dictionary2['cross_section'] = float(dato)
		#print(float(dato))
		else: 
			self.dictionary2['cross_section'] = -1
		self.newlist2.append([self.dictionary2['Mh'],self.dictionay2['laphi'],self.dictionay2['laSH1'],self.dictionay2['Mp1'],self.dictionay2['mu32'],self.dictionay2['cross_section']]) 

def ejecutarOmega(direc,dictionary):
	mo1 = Model(dictionary)
	for irun in range(0.5000,1): 
		if(irun%100 == 0 ): 
			print('irun='+str(irun) + ' time='+str(time.process_time()))
	
		Mp1 = np.random.uniform(1000,10000) 
		#las1 = 10**( (log10(5e-2)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
		las1 = np.random.uniform(1e-4,1)
		mu1 = np.random.uniform(10,1000)
		dictionary['Mp1'] = Mp1 
		dictionary['laSH1'] = las1 
		dictionary['mu32'] = mu1 
		

if __name__ = '__main__': 
	dataD1 = {'Mh':125, 'laphi':0.07,'laSH1':0.1,'Mp1':300,'mu32':1000,'Mtop':173.2} #Diccionario con los datos del archivo.
	