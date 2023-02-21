import numpy as np 
import pandas as pd 

datos = np.loadtxt('Datos.txt')
df = pd.DataFrame(datos,columns=['MH','laphi','laSH','Mp','mu3','Mtop'])


