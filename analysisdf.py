import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
from scipy import stats

df0 = pd.read_csv('Raw_Data_0degrees.csv')
df30 = pd.read_csv('Raw_Data_30degrees.csv')

#renaming for simplicity
df0 = df0.rename(columns = {"Time (s)":"time","Acceleration x (m/s^2)":"gx","Acceleration y (m/s^2)":"gy","Acceleration z (m/s^2)":"gz","Absolute acceleration (m/s^2)":"a"})
df30 = df30.rename(columns = {"Time (s)":"time","Acceleration x (m/s^2)":"gx","Acceleration y (m/s^2)":"gy","Acceleration z (m/s^2)":"gz","Absolute acceleration (m/s^2)":"a"})


print(df0)
print(df30)

print(df0.describe())
print(df0.count())



df0.plot(x='time')
plt.xlabel('Tempo [s]')
plt.ylabel('Accelerazione [m/$s^2$]')
plt.title(r'$g_x$ $g_y$ $g_z$ e |$\vec {g}$|  in funzione del tempo')
plt.savefig('gs_time.png')

df30.plot(x='time',y='gz')
plt.xlabel('Tempo [s]')
plt.ylabel('Accelerazione z [m/$s^2$]')
plt.show()

df0[['gx','gy','gz','a']].std().plot(kind='bar')
plt.show()

df0["gz"].hist(bins=100)
plt.show()

#estraggo le informgzioni per praticità
mean0 = df0.mean()
median0 = df0.median()
std0 = df0.std()
print(mean0['gz'])

mean30 =df30.mean()
median30 = df30.median()
std30 = df30.std()

binsize = df0["gz"].std(ddof=1)/15 # metà della standard deviation
interval = df0["gz"].max() - df0["gz"].min()
nbins = int(interval / binsize)

print(nbins)
plt.hist(df0["gz"],bins=nbins,color="blue",alpha=0.75)
plt.xlabel('Accelerazione $g_z$ [m/$s^2$]')
plt.ylabel('Numero di misure')
plt.title(label='Istogramma di $a_z$: $\mu$={0:.3f} m/$s^2$ $\sigma$={1:.3f} m/$s^2$'.format(mean0['gz'],std0['gz']))


lnspc = np.linspace(df0['gz'].min()-std0['gz'],df0['gz'].max()+std0['gz'])
norm_factor = df0['gz'].size * binsize

f_gaus = norm_factor*stats.norm.pdf(lnspc,mean0['gz'],std0['gz'])
plt.plot(lnspc,f_gaus,linewidth=1,color='r',linestyle='--')
plt.show()
