import numpy as np 
import matplotlib.pyplot as plt 

datos = np.loadtxt("unionDatos.txt")
print(len(datos))
#print(datos)


x = [] 
y = [] 
z = []
for i in range(len(datos)): 
	x.append(datos[i][1])
	y.append(datos[i][3]*1e-34)
	z.append(datos[i][2])

fig, ax = plt.subplots(figsize=(9,7)) 

#ax.set_ylabel('Y label',loc='top')
#ax.set_xlabel('XLabel',loc='left') 
ax.set_xscale('log')
ax.set_yscale('log')
im = ax.scatter(x,y,c=z,cmap='viridis')
fig.colorbar(im)
#plt.xlim(0,1000)
plt.title("Singlete escalar con simetría $Z_{3}$")
plt.ylabel("$\sigma_{SI}/cm^{2}$")
plt.xlabel("Mass DM (GeV)")
plt.savefig('mapeo_de_datos.jpg')
plt.show()
