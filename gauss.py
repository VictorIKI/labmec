import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return 1/(np.sqrt(2*np.pi)*sig)*np.exp(-np.power(x-mu,2.)/(2*np.power(sig,2.)))

x_min=129#float(input("Valore minimo di x:"))
x_max=149#float(input("Valore massimo di x:"))
mu=138.2#float(input("inserisci mu:"))
sig=4.58#float(input("inserisci sigma:"))
X=[x_min,x_max]
Z=(X-mu)/sig
f_x = gaussian(X,mu,sig)
print(Z)
#F_x = integrate.quad(gaussian(X,mu,sig),-np.inf,np.inf)
T_z=integrate.quad(lambda y: 1/(np.sqrt(2*np.pi))*np.exp(0.5*np.power(Z,2),0,z))
plt.scatter(np.linspace(0,10),f_x)
plt.show()
