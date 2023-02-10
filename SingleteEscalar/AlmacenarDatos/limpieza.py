import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
archivo = open('Datos.txt')
datos=[]
for linea in archivo: 
	datos.append(linea.split())

archivo.close()

df = pd.DataFrame(datos,columns=['Mass DM','SSHH','Omega'])
df = df.drop_duplicates(df.columns[df.columns.isin(['Mass DM'])],keep='first')
df.drop(df.index[-1],inplace=True)
df.drop_duplicates(['SSHH'],keep='last')

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


plt.figure(figsize=(9,7)) 
plt.title("Scalar Singlet",fontsize=25)
plt.plot(X,Y,'k.',label='$\Omega h^{2} = 0.12$')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("$M_{s} (Gev)$",fontsize=20)
plt.ylabel("$\lambda_{sh}$",fontsize=20)
plt.legend(fontsize=20)
plt.grid()
plt.savefig('Real_Scalar_Singlet.svg')
plt.show()
