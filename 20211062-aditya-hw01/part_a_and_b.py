import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#compute x_hat
def compute_x_hat(y_means, y_var):
    y_var_sq= [i**2 for i in y_var]
    x_hat_num= np.sum([y_means[i]/y_var_sq[i] for i in range(len(y_means))])
    x_hat_denom= np.sum([1/i for i in y_var_sq])
    x_hat= x_hat_num/ x_hat_denom
    sig= np.sqrt(1/x_hat_denom)
    return x_hat, sig

#part (a), (b); fix sigma2 and vary y2 and vice versa
fixed_sig_2= 2.0
varied_y2_arr= np.arange(-5, 5.5, 0.5)
store_x_hat_varied_y2=[]

fixed_y2= 1.0
varied_sig2_arr= np.arange(0, 5.5, 0.5)
varied_sig2_arr_sq= [i**2 for i in varied_sig2_arr]
store_x_hat_varied_sig2=[]

for y2 in varied_y2_arr:
    y_means= [0.0, y2]
    y_var= [1.0, fixed_sig_2]
    x_hat, sig= compute_x_hat(y_means, y_var)
    store_x_hat_varied_y2.append(x_hat)

for sig2 in varied_sig2_arr:
    y_means= [0.0, fixed_y2]
    y_var= [1.0, sig2]
    x_hat, sig= compute_x_hat(y_means, y_var)
    store_x_hat_varied_sig2.append(x_hat)   

plt.plot(varied_sig2_arr, store_x_hat_varied_sig2, label="fixed y2")
plt.plot(varied_y2_arr, store_x_hat_varied_y2, label= "fixed sigma2")
plt.title("x_hat with different values of y2 and sigma2")
plt.legend()
plt.show()