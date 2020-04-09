import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import stats
import pandas as pd

data = np.array([21.802, 21.810, 21.801, 21.816, 21.811, 21.810, 21.810, 21.806, 21.811, 21.830, 21.806, 21.830, 21.806, 21.820, 21.821, 21.815, 21.810, 21.799, 21.790, 21.779, 21.821, 21.794, 21.794, 21.816, 21.820, 21.797, 21.832, 21.788, 21.803, 21.829])



print(data)

N= data.size

print("type: ",type(data))
print("size:\t",data.size)
print("dimension:\t", data.ndim)
print("shape: ", data.shape)
print("data type: ",data.dtype)

data_list = data.tolist()
data_list

rounded_data = np.round(data,2)
print(rounded_data)


mean1=np.mean(data)
mean2=np.sum(data)/N
mean3= data.mean()
mean4 =data.sum()/N

print('mean1 = {0}, mean2 = {1}, mean3 = {2}, mean4 = {3}'.format( mean1, mean2, mean3, mean4) )

print('mean1 = {0:.0f}, mean2 = {1:.1f}, mean3 = {2:.2f}, mean4 = {3:.3f}'.format( mean1, mean2, mean3, mean4) )

sorted_data = np.sort(data)
print(sorted_data)

if N%2:
    median1=sorted_data[round(0.5*(N-1))]
else:
    index = round(0.5*N)
    median1 = 0.5 * (sorted_data[index-1] + sorted_data[index])

median2 = np.median(data)

print('median1 = {0}, median2 = {1}'.format( median1, median2) )
var1 = np.var(data,ddof=1)
std1 = var1 ** 0.5 # a ** x = a^x

#std2
std2 = np.std(data,ddof=1)
#std3
var3 = ((data-data.mean())**2).sum()/(N-1)
std3 = var3 ** 0.5

res = 0.
for x in np.nditer(data):
    res += (x-data.mean()) ** 2
    print('value = {0}, (value-mean)^2 = {1}'.format( x , res) )
var4 = res / (N-1)
std4 = var4 ** 0.5

print('std1 = {0}, std2 = {1}, std3 = {2}, std4 = {3}'.format( std1 , std2, std3, std4) )

binsize = np.std(data,ddof=1)/2 # half of standard deviation
interval = data.max() - data.min()
nbins = int(interval / binsize)
nbins
counts , bins , patches = plt.hist(data,bins=nbins,color="blue",alpha=0.75)
plt.xlabel('x [mm]')
plt.ylabel('Entries')
plt.title(label='Histogram of x: $\mu$={0:.3f} $\sigma$={1:.3f}'.format(mean1,std1))

# ==> draw a gaussian function
# create an array with 100 equally separated values in the x axis interval
lnspc = np.linspace(data.min()-data.std(), data.max()+data.std(), 100)
# create an array with f(x) values, one for each of the above points
# normalize properly the function such that integral from -inf to +inf is the total number of events
norm_factor = data.size * binsize
f_gaus = norm_factor*stats.norm.pdf(lnspc,data.mean(),data.std())
# draw the function
plt.plot(lnspc, f_gaus, linewidth=1, color='r',linestyle='--')
