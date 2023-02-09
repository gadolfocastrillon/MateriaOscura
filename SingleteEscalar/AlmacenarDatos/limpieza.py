import pandas as pd 
import matplotlib.pyplot as plt 

archivo = open('Datos.txt')
datos=[]
for linea in archivo: 
	datos.append(linea.split())

archivo.close()

df = pd.DataFrame(datos,columns=['Mass DM','SSHH','Omega'])
df = df.drop_duplicates(df.columns[df.columns.isin(['Mass DM'])],keep='first')
df.drop(df.index[-1],inplace=True)

X = [] 
for i in df['Mass DM']: 
	try: 
		X.append(float(i))
	except: 
		pass


Y=[]
for i in df['SSHH']: 
	try: 
		Y.append(float(i))
	except: 
		pass

plt.figure() 
plt.plot(X,Y,'.')
plt.show()
