import numpy as np 
import subprocess 
import matplotlib.pyplot as plt 
import time 

class Modelo: 
	def __init__(self.dictionary): 
		self.dictionary = dictionary
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

