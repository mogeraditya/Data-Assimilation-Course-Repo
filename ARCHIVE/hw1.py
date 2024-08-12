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
varied_sig2_arr= np.arange(-5, 5.5, 0.5)
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

# plt.plot(varied_sig2_arr, store_x_hat_varied_sig2)
# plt.plot(varied_y2_arr, store_x_hat_varied_y2)
# plt.show()

#generate data for 3d plot
fig = plt.figure()#figsize = (10, 7))
ax = plt.axes(projection ="3d")

X,Y,Z= [], [], []
for y2 in varied_y2_arr:
    fix_y2_arr=[]
    for sig2 in varied_sig2_arr:
        y_means= [0.0, y2]
        y_var= [1.0, sig2]
        x_hat, sig= compute_x_hat(y_means, y_var)

        X.append(y2)
        Y.append(sig2**2)
        Z.append(x_hat)
        fix_y2_arr.append(x_hat)
    ax.plot(varied_sig2_arr_sq, fix_y2_arr, zs= -5, zdir='x', label='curve in (x, y)')

for sig2 in varied_sig2_arr:
    fix_sig2_arr=[]
    for y2 in varied_y2_arr:
        y_means= [0.0, y2]
        y_var= [1.0, sig2]
        x_hat, sig= compute_x_hat(y_means, y_var)
        fix_sig2_arr.append(x_hat)
    ax.plot(varied_y2_arr, fix_sig2_arr, zs= -5, zdir='y', label='curve in (x, y)')

# ax.scatter(X, Z, zs= -5, zdir='y', label='curve in (x, y)')
# ax.scatter(Y, Z, zs= -5, zdir='x', label='curve in (x, y)')
ax.scatter3D(X, Y, Z, color = "green")
ax.set_xlabel('Y2')
ax.set_ylabel('sig2^2')
ax.set_zlabel('X_hat')
plt.title("")
plt.show()




