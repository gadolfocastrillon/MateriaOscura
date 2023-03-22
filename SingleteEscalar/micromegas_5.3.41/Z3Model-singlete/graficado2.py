import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

datos = np.loadtxt('DatosCSDD.txt') 
newlist = [] 
print(len(datos))
for dat in datos: 
	if (dat[4] < np.sqrt(8)*dat[3]): 

		newlist.append(dat)

print(len(newlist))
