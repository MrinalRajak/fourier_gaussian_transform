
#Prove that fourier transform of gaussian is gaussian

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2)
a=-10.0
b=10.0
x=np.arange(a,b,0.1)
R=[]
I=[]
for k in np.arange(a,b,0.1):
    R.append(quad(lambda x:f(x)*np.cos(k*x),a,b)[0])
for k in np.arange(a,b,0.1):
    I.append(quad(lambda x:f(x)*np.sin(k*x),a,b)[0])

k1=np.arange(a,b,0.1)
fig,(ax0,ax1)=plt.subplots(ncols=2)
ax0.plot(x,f(x),lw=2,ls='--',c='green')
ax0.set_title(r'$x-e^{-x^2}$',fontsize=20)
ax1.plot(x,f(x),lw=2,ls='-',c='red')
ax1.set_title(r'$k-F(k)$',fontsize=20)
plt.show()
