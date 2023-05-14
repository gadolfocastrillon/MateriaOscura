from rutinas import d_indirecta, omega
import numpy as np

#X = [0.410235241165042,199.7017885254824,498.59987685938177]
def mostrar_valores(X):
	sigma_v,ot = d_indirecta(X)
	print('\n')
	print("El valor de omega es: ")
	print(omega(X))
	print("\n")
	print("El valor para sigma_v es: " + str(sigma_v))
	for i in ot: 
		print("El valor de un canal es: " + str(i))

def guardar_datos(X,SIGMA,OT): 
	n = int(len(SIGMA))
	archivo = open("datosSigma.txt",'w')
	for i in range(n): 
		for valor in X[i]: 
			archivo.write(str(valor) + " ") 
		archivo.write(str(SIGMA[i]) + " ")
		for valor in OT[i]: 
			#print(valor)
			archivo.write(str(valor) + " ")
		archivo.write("\n")
	archivo.close()

if __name__ == '__main__': 
	#dat = np.loadtxt('AlmacenarDatos/unionDatos70-1000.txt')
	dat = np.loadtxt('todos-los-datos.txt')
	x = dat.T[0]
	y = dat.T[1]
	z = dat.T[2]
	n = len(x)

	X = [[x[i],y[i],z[i]] for i in range(n)]
	SIGMA = [] 
	OT = [] 
	sltn = 0 
	part = 100
	m=0 #Para mostrar en pantalla 
	if(n%part == 0): 
		val = n/part
	else: 
		val = (n - n%part)/part
	#print(val/10)
	print("Runing algoritm")
	for x in X: 
		if (sltn%val == 0): 
			print("["+"*"*m + "]"+ str(m) +"%",end='\r')
			m+=1
		sigma_v,channels = d_indirecta(x)
		SIGMA.append(sigma_v)
		#print(sigma_v)
		OT.append(channels) 
		#print(channels)
		sltn+=1 
	print("[**********]100%")
	print("Programa completado")
	guardar_datos(X,SIGMA,OT)
