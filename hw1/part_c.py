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

#part (c); generate data for 3d plot

varied_y2_arr= np.arange(-5, 5.5, 0.5)
varied_sig2_arr= np.arange(0, 5.5, 0.5)
varied_sig2_arr_sq= [i**2 for i in varied_sig2_arr]

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
        Y.append(sig2)
        Z.append(x_hat)
        fix_y2_arr.append(x_hat)
    ax.plot(varied_sig2_arr, fix_y2_arr, zs= -5, zdir='x', label='curve in (x, y)') #PROJECTIONS

for sig2 in varied_sig2_arr:
    fix_sig2_arr=[]
    for y2 in varied_y2_arr:
        y_means= [0.0, y2]
        y_var= [1.0, sig2]
        x_hat, sig= compute_x_hat(y_means, y_var)
        fix_sig2_arr.append(x_hat)
    ax.plot(varied_y2_arr, fix_sig2_arr, zs= 0, zdir='y', label='curve in (x, y)') #PROJECTIONS

ax.scatter3D(X, Y, Z, color = "green")
ax.set_xlabel('Y2')
ax.set_ylabel('sig2')
ax.set_zlabel('X_hat')
plt.title("")
plt.show()

#Note; 3D plot is the scatter plot.
#PROJECTIONS help us see changes in plots made in (a) and (b) at different values of the fixed parameters.