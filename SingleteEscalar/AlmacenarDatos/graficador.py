import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

df = pd.read_csv('InteraccionDM-P.csv')

X = df['Mass DM']
Y = df['SI 1']
Y2 = df['SI 2']

plt.figure(figsize=(9,7)) 
plt.title('Interaccion DM-Proton (Amplitud)',fontsize=25)
plt.xlabel('Masa (Gev)',fontsize=20)
plt.ylabel('Amplitud',fontsize=20)
plt.plot(X,Y,'k.',label='$\Omega h^{2} = 0.12$')
plt.xscale('log')
plt.yscale('log') 
plt.rc('axes',labelsize=30)
plt.legend(fontsize=20)
plt.savefig('InteraccionDM-P-amplitud.svg')
plt.show()

plt.figure(figsize=(9,7)) 
plt.title('Interaccion DM-Proton (Cross sections)',fontsize=25)
plt.xlabel('Masa (Gev)',fontsize=20)
plt.ylabel('Cross sections',fontsize=20)
plt.plot(X,Y2,'k.',label='$\Omega h^{2} = 0.12$')
plt.xscale('log')
plt.yscale('log') 
plt.rc('axes',labelsize=30)
plt.legend(fontsize=20)
plt.savefig('InteraccionDM-P-cross_sections.svg')
plt.show()

