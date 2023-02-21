#!/usr/bin/env python

#import pandas as pd
import numpy as np
#from scipy.interpolate import interp1d
#import matplotlib.pyplot as plt
#from matplotlib.colors import LogNorm
from numpy import *
#from scipy.integrate  import quad
import cmath

import subprocess
import sys


def writeinputf(file,dictionary):
    ''' write dictionarys parameters in file'''
    data1 = open(file,'w')
    for items in dictionary.items():
        data1.write("%s %s\n" % items)

    data1.close()


newlist1=[ ]

datapar={"MH": 125.0, "Mp1": 300, "Mp2": 350, "Mp3": 400, "las1": 0.1, "las2": 0.1, "las3": 0.1, "la412": 0.1, "la413": 0.1, "la423": 0.1, "mus1": 100.0, "mus2": 100.0, "mus3": 100.0, "mus4": 100.0, "la31": 0.01, "la32": 0.01, "la33": 0.01, "la34": 0.01, "la35": 0.01, "la36": 0.01}

sltns=0

MH   =  125.
MP1  = 300
MP2  = 350
MP3  = 400 
LAS1 = 0.1
LAS2 = 0.1
LAS3 = 0.1
LA412 = 0.0 
LA413 = 0.0 
LA423 = 0.0 
MUS1  = 0.0
MUS2  = 0.0
MUS3  = 0.0
MUS4  = 0.0
LA31 = 0.0 
LA32 = 0.0 
LA33 = 0.0 
LA34 = 0.0 
LA35 = 0.0 
LA36 = 0.0 

datapar['MH']    = MH
datapar['Mp1']   = MP1
datapar['Mp2']   = MP2
datapar['Mp3']   = MP3
datapar['las1']  = LAS1
datapar['las2']  = LAS2
datapar['las3']  = LAS3
datapar['la412'] = LA412
datapar['la413'] = LA413
datapar['la423'] = LA423
datapar['mus1']  = MUS1
datapar['mus2']  = MUS2
datapar['mus3']  = MUS3
datapar['mus4']  = MUS4
datapar['la31'] = LA31
datapar['la32'] = LA32
datapar['la33'] = LA33
datapar['la34'] = LA34
datapar['la35'] = LA35
datapar['la36'] = LA36



sltns=0
for irun in range(0,8001,1):
    if (irun%100==0):
        print ('irun=',irun)
    omega1 = 0.0
    omega2 = 0.0
    #sigmaSI1 = -1.0
    #sigmaSI2 = -1.0
    #pval1 = -1.0
    #pval2 = -1.0
    #
    MP1  = np.random.uniform(100,400)
    MP2  = np.random.uniform(1.01,1.3)*MP1
    #MP3  = np.random.uniform(1.01,1.99)*MP2
    MP3  = np.random.uniform(1.01*MP2,0.99*(MP1+MP2))
    #MP3  = np.random.uniform(1.01*MP2,1.25*MP2)
    #if (MP3 < MP1+MP2): #MP2 < 2*MP1 and MP3 < 2*MP2 and MP1 < 2*MP3 and MP1 < MP2+MP3 and MP2 < MP1+MP3 and 
    LAS1  = 10**( (log10(5e-2)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LAS2  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LAS3  = 10**( (log10(1e0)-log10(1e-2))*np.random.uniform(0,1)+log10(1e-2))*(-1)**np.random.randint(0,2)
    LA412 = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    #LA412 = np.random.uniform(0.1,1)*(-1)**np.random.randint(0,2)
    LA413 = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LA423 = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    #LA423 = np.random.uniform(0.1,1)*(-1)**np.random.randint(0,2)
    LA31  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LA32  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LA33  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LA34  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LA35  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
    LA36  = 10**( (log10(1e0)-log10(1e-4))*np.random.uniform(0,1)+log10(1e-4))*(-1)**np.random.randint(0,2)
#    MUS1  = 10**( (log10(1e4)-log10(1e2))*np.random.uniform(0,1)+log10(1e2))
#    MUS2  = 10**( (log10(1e4)-log10(1e2))*np.random.uniform(0,1)+log10(1e2))
    #MUS3  = 10**( (log10(1e4)-log10(1e2))*np.random.uniform(0,1)+log10(1e2))
    MUS3  = np.random.uniform(1000,10000)
    #MUS4  = 10**( (log10(1e4)-log10(1e2))*np.random.uniform(0,1)+log10(1e2))
    #MUS4  = np.random.uniform(100,1000)
    # writing data.dat input file for micromegas
    datapar['Mp1']   = MP1
    datapar['Mp2']   = MP2
    datapar['Mp3']   = MP3
    datapar['las1']  = LAS1
    datapar['las2']  = LAS2
    datapar['las3']  = LAS3
    datapar['la412'] = LA412
    datapar['la413'] = LA413
    datapar['la423'] = LA423
    datapar['la31']  = LA31
    datapar['la32']  = LA32
    datapar['la33']  = LA33
    datapar['la34']  = LA34
    datapar['la35']  = LA35
    datapar['la36']  = LA36
    #datapar['mus1']  = MUS1
    #datapar['mus2']  = MUS2
    datapar['mus3']  = MUS3
#    datapar['mus4']  = MUS4
    
    writeinputf('data.dat',datapar)
    # running micromegas and extracting the relic density (omega)
    subprocess.getoutput("./main data.dat > output.dat")
    aa=subprocess.getoutput("grep 'omega1' output.dat | awk -F'=' '{print $4}' | awk -F' ' '{print $1}'")
    bb=subprocess.getoutput("grep 'omega2' output.dat | awk -F'=' '{print $5}' | awk -F' ' '{print $1}'")
    cc=subprocess.getoutput("grep 'omega3' output.dat | awk -F'=' '{print $6}' | awk -F' ' '{print $1}'") 
    if ( len(aa)>0 and len(bb)>0 and len(cc)>0 ):
        omega1 = float(aa)
        omega2 = float(bb)
        omega3 = float(cc)
    else:
        omega1 = -1.0
        omega2 = -1.0 
        omega3 = -1.0
        #print (omega1,omega2)
    #print (omega1,omega2,omega3)
    omega=omega1+omega2+omega3
    if ((omega1 > 0.0) and (omega2 > 0.0) and (omega3 > 0.0) and (omega > 0.11) and (omega < 0.13)):
        sltns=sltns+1
        newlist1.append([MP1,MP2,MP3,omega1,omega2,omega3,LAS1,LAS2,LAS3,LA412,LA413,LA423,LA31,LA32,LA33,LA34,LA35,LA36,MUS1,MUS2,MUS3,MUS4]) 
        #    break                                                                                                 
        #if (omega1 < 0.1018):                                                                                        
        #    break                                                                                                  
                                                                                                                    
print ('sltns=',sltns)                                                                                               
datos = np.asarray(newlist1)
np.savetxt('nuevosdatos.txt',datos)
