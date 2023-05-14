import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

datos = np.loadtxt('dLikelihood.txt')
#df = pd.DataFrame(datos,columns=['MH','laphi','laSH','Mp','mu3','Mtop'])
print(len(datos))
'''
fig, ax = plt.subplots() 

#ax.set_ylabel('Y label',loc='top')
#ax.set_xlabel('XLabel',loc='left') 
ax.set_xscale('log')
ax.set_yscale('log')
im = ax.scatter(df['Mp'],df['cs'],c=df['mu3'],cmap='viridis')
fig.colorbar(im)
plt.savefig('figura de prueba2.svg')
plt.show()

plt.figure()

plt.plot(df['Mp'],df['mu3'],'k.')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0,1000)
plt.savefig('figura de prueba.svg')
plt.show()
'''
