import numpy as np 
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt 
import time 

xobs =[]
min_ = -5
max_ = 5 
dim = 4
bounds[(min_,max_)]*dim

def samples_inside(x,chi_sq): 
    delta_chi_sq = chi_sq - min_chi_sq
    inside = delta_chi_sq <= critical_chi_sq
    return x[:, inside]

def gaussian(x): 
	sigma = 0.012
	return (x-xobs)/sigma

def gaussian_general(x): 
	n = len(x) 
	return sum(gaussian(x[i]) for i in range(n-1))


def de_scan(dim,round_to_nearest=None): 
	x = [] 
	chi_sq = [] 

	def objective(x_): 
		chi_sq_ = gaussian_general(x_) 
		chi_sq.append(chi_sq_) 
		x.append(x_) 
		return chi_sq_

	differential_evolution(objective, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=seed)
	if round_to_nearest is not None: 
		if round_to_nearest is not None: 
        len_x = len(x)
        print(len(x)%round_to_nearest) 
        keep_n = len_x - (len_x %round_to_nearest)
        x = x[:keep_n]
        chi_sq = chi_sq[:keep_n] 
    
    return samples_inside(np.array(x).T, np.array(chi_sq)), len(x)


if __name__ == '__main__': 
	np.random.seed(seed) 
	plt.figure(figsize=(10,10))
	print("Running de_scan") 
	t0 = time.time()
	x, calls = de_scan(dim,round_to_nearest=1000) 
	de_time = time.time() - t0 
	print("Plotting de_scan") 
	print(r'Tiempo de ejecución : '+ str(de_time))
	plt.scatter(x[0][0], x[1][0], s=30, edgecolor='0.05',
                linewidth=0.25, alpha=1.0, facecolor=de_pts,
                label=r'Differential evolution: \num{{{:d}}} out of \num{{{:d}}} points'
                .format(x.shape[1], calls))
    
    #print(de_scatter)
    plt.title("Función de Rosenbrock")
    plt.xlabel("parametro X1") 
    plt.ylabel("Parametro X2")
    plt.savefig("Grafico_Rosenbrock.svg")
    plt.show()