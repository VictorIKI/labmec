import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
from scipy import stats

#importo i file su variabili separate
t,ax,ay,az,a = np.loadtxt('Raw_Data_0_degree.csv', unpack=True,skiprows=1)

#medie
mean_az = az.mean()
mean_ax = ax.mean()
mean_ay = ay.mean()

#deviazioni standard
std_ax = ax.std()
std_ay = ay.std()
std_az = az.std()

#mediane
median_ax = np.median(ax)
median_ay = np.median(ay)
median_az = np.median(az)

print(std_az)
print(mean_az)
print(median_az)

binsize = az.std(ddof=1)/2
interval = az.max() - az.min()
nbins = int(interval/binsize)


lnspc = np.linspace(az.min()-az.std(),az.max()+az.std(),100)
norm_factor = az.size * binsize

f_gaus = norm_factor*stats.norm.pdf(lnspc,mean_az,std_az)


plt.plot(lnspc, f_gaus, linewidth=1, color='r',linestyle='--')

plt.title(label='Istogramma di $a_z$: $\mu$={0:.3f} m/$s^2$ $\sigma$={1:.3f} m/$s^2$'.format(mean_az,std_az))
plt.hist(az,bins=nbins)
counts , bins , patches = plt.hist(az,bins=nbins,color="blue",alpha=0.75)
print(counts)
print(bins)
print(patches)
plt.show()
