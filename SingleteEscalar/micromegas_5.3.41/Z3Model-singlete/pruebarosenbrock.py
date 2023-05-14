import time 
import numpy as np 
from scipy.optimize import differential_evolution
from scipy.stats import chi2
import matplotlib.pyplot as plt

n_random_samples = int(1e7)
dim = 3
min_ = -5.
max_ = 5.
seed = 127

min_chi_sq = 0.
alpha = 0.05
critical_chi_sq = chi2.isf(alpha,2)
print(critical_chi_sq)
# Color style for output sample points
de_pts = "#91bfdb" # Diver scan
rn_pts = "#fc8d59" # Random scan
gd_pts = "#ffffbf" # Grid scan

def rosenbrock(x, y):
    """
    @returns Rosenbrock function
    """
    a = 1.
    b = 100.
    return (a - x)**2 + b * (y - x**2)**2


def gaussian(x):
    sigma = np.sqrt((0.1*x)**2 + (0.001)**2) #Defino el sigma 
    xobs = 0.120 #densidad reliquia observable
    return ((x-xobs)/sigma)**2 #Gaussiana

def rosenbrock_general(x):
    """
    @returns Generalization of Rosenbrock function
    """
    n = len(x)
    return sum(gaussian(x[i]) for i in range(n - 1))
    #return gaussian(x)
    #return sum(rosenbrock(x[i], x[i+1]) for i in range(n - 1))

def loglike(x):
    """
    @returns Log-likelihood
    """
    return -rosenbrock_general(x)

def samples_inside(x,chi_sq): 
    delta_chi_sq = chi_sq - min_chi_sq
    inside = delta_chi_sq <= critical_chi_sq
    #print(x[:,inside])
    return x[:, inside]

def writer2(x,file):
    data = open(file,'w') 
    #me guarda los datos de masa, lahs, mu3 y cross section
    for i in x: 
        texto = str(i[0]) + " " + str(i[1]) + " " +str(i[2])+ " " + str(i[3]) +"\n"
        data.write(texto)
    data.close()

def de_scan(dim, round_to_nearest=None):
    """
    @returns Points from within delta chi-squared contour from differential evolution
    and number of calls
    """
    bounds = [(min_, max_)] * dim
    x = []
    chi_sq = []
    cs = []
    def objective(x_):
        """
        @returns Objective for DE that saves chi-squared and parameters
        """
        chi_sq_ = -2. * loglike(x_)
        chi_sq.append(chi_sq_)
        cs.append(1)
        x.append(x_)
        return chi_sq_

    differential_evolution(objective, bounds,
                           strategy='rand1bin', maxiter=None,
                           popsize=50, tol=0.01, mutation=(0.7, 1.99999), recombination=0.15,
                           polish=False, seed=seed)
    #print(combinacion(x,cs))

    valor = np.array(x).T 
    datos=[valor[i] for i in range(len(valor))]
    #print(len(valor))
    datos.append(cs)
    #print(np.array(datos))
    #samples_inside(np.array(datos),np.array(chi_sq))

    if round_to_nearest is not None:
        len_x = len(x)
        keep_n = len_x - (len_x % round_to_nearest)
        x = x[:keep_n]
        chi_sq = chi_sq[:keep_n]
 
    return samples_inside(np.array(datos),np.array(chi_sq)),len(x)

if __name__ == '__main__': 
	#np.random.seed(seed) 

    plt.figure(figsize=(10,7))
    x, calls = de_scan(dim)
    writer2(x.T,'ddddd.txt')
    #print(x.T)
    plt.scatter(x[3], x[0], s=30, edgecolor='0.05',
                linewidth=0.25, alpha=1.0, facecolor=de_pts,
                label=r'Differential evolution: \num{{{:d}}} out of \num{{{:d}}} points'
                .format(x.shape[1], calls))
    #plt.show()

	