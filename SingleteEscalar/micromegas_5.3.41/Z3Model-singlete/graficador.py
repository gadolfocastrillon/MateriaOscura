import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

datos = np.loadtxt('DatosCSDD.txt')
df = pd.DataFrame(datos,columns=['MH','laphi','laSH','Mp','mu3','cs'])


fig, ax = plt.subplots(figsize=(9,7)) 

#ax.set_ylabel('Y label',loc='top')
#ax.set_xlabel('XLabel',loc='left') 
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
'''
plt.figure(figsize=(9,7))

plt.plot(df['Mp'],df['cs'],'k.')
plt.xscale('log')
plt.yscale('log')
plt.savefig('AlmacenarDatos/modeloZ3.svg')
plt.xlim(0,1000)
plt.show()
'''
