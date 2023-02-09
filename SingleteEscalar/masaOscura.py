class Moscura: 
	def __init__(self): 
		self.comando = './main data2.par>temporal.dat' 
		#Comando para ejecutar el programa de materia oscura
		self.almacenarDatos = 'datos.txt'
		self.archivo = '/Escritorio/trabajo_de_grado/micromegas_5.3.41/SingletDM/data2.par'
		self.inicioM = 10 #Inicio de la masa 
		self.finalM = 10000 #Final de la masa 
		self.pasoM = 1
		self.inicioSH = 0.0001 #Inicio del termino interacion
		self.finalSH = 1 #Final del termino interacion 
		self.pasoSH= 0.001
		#Rango de error alrededor de 0.12, error del 10%
		self.topValor = 0.121 
		self.lowValor = 0.119
		self.detener = False 

	#Las funciones con e permiten editar los valores que tienen las variables
	#Las funciones con m permiten mostrar los valores que tienen las variables  
	def eInicioM(self,valor): 
		self.inicioM = valor 
	def eFinalM(self,valor): 
		self.finalM = valor 
	def ePasoM(self,valor): 
		self.pasoM = valor 
	def mInicioM(self): 
		return self.inicioM 
	def mFinalM(self): 
		return self.finalM 
	def mPasoM(self): 
		return pasoM	
	def eInicioSH(self,valor): 
		self.inicioSH = valor 
	def eFinalSH(self,valor): 
		self.finalSH = valor 
	def ePasoSH(self,valor): 
		self.pasoSH = valor 
	def mInicioSH(self): 
		return self.inicioSH 
	def mFinalSH(self): 
		return self.finalSH 
	def mPasoSH(self): 
		return self.pasoSH 


	def editar(self,Mdm1,laSH): 
		datos = []
		for linea in open(self.archivo): 
			datos.append(linea) 
		datos[3] = 'laSH'+'   '+str(laSH)+'\n'
		datos[4] = 'Mdm1' + '   '+ str(Mdm1)+'\n'
		return datos 

	def escribir(self,datos):
		archivo = open(self.archivo,'w')
		for i in datos: 
			archivo.write(i)
		archivo.close() 

	def analisis(self,Mdm1,laSH): 
		import re
		datos = [] 
		for linea in open('temporal.dat'): 
			datos.append(linea) 

		archivo = open(self.almacenarDatos,'a') 

		val = float(datos[9].split('=')[2])
		if((val<=self.topValor)&(val>=self.lowValor)): 
			print(str(Mdm1) + '	' +str(laSH)+ '	' +str(val))
			archivo.write(str(Mdm1) + '	' +str(laSH)+ '	' +str(val)+'\n')
			datos = []
			self.detener = True 
		archivo.close()
	
	def ejecutar(self): 
		import numpy as np 
		import os 
		for i in np.arange(self.inicioM,self.finalM,self.pasoM): 
			self.detener = False 
			for j in np.arange(self.inicioSH, self.finalSH, self.pasoSH):
				datos = self.editar(i,j) 
				self.escribir(datos)
				os.system(self.comando)
				self.analisis(i,j)	
				if self.detener: 
					break