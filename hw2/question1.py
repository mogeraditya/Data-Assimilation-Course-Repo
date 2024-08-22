import numpy as np
import scipy as scp
import numpy.linalg as npla
import matplotlib.pyplot as plt
import math
import skimage
import os
# parameters needed to define a 2-dim Gaussian:
# means [m1, m2], std.dev. [s1, s2], and correlation [rho]
s1 = 1.0; s2 = 2.0; rho = 0.85; m1 = 1.7; m2 = 9.4

sig = np.array([[s1*s1, s1*s2*rho], [s1*s2*rho, s2*s2]])
mu = np.array([m1, m2])
a,b,c= s1*s1, s1*s2*rho, s2*s2
# number of points creating a grid for plotting
npts = 30
x1 = np.linspace(m1 - 2.5*s1, m1 + 2.5*s1, npts)
x2 = np.linspace(m2 - 2.5*s2, m2 + 2.5*s2, npts)
xg, yg = np.meshgrid(x1, x2)
pos = np.dstack((xg, yg))

# compute the Gaussian density
npdf = scp.stats.multivariate_normal.pdf(pos, mean = mu, cov = sig)

#refer to the written solution for constants used. 
#k is the constant ln(1/ [(2*c*pi)**2 * det(sig)])
c= 0.01
def compute_k_given_c(c, sig):
    q= (2*np.pi*c)**2
    sig_det= npla.det(sig)
    print(sig_det)
    k= np.log(1/(q*sig_det))
    return k

eigenvalues= np.sort(npla.eig(sig)[0])
lambda2, lambda1= eigenvalues

k= compute_k_given_c(c, sig)
length_major_axis= np.sqrt(lambda1*k)
length_minor_axis= np.sqrt(lambda2*k)
print(length_major_axis, length_minor_axis)
print(npla.eig(sig)[1].T[0])
print(npla.eig(sig)[0][0])
m= (lambda1- a)/ b

print(m)
theta= math.atan(m)
print((theta*180)/np.pi)
x=x1#np.arange(-1,5, 1)

# plt.figure(figsize=(12,6))
plt.plot(x, [(i*m+ m2- m*m1) for i in x], color= "red")
plt.plot(x, np.array([(i*(-1/m)+ m2- (-1/m)*m1) for i in x]), color= "red")
# rr,cc= skimage.draw.ellipse_perimeter(r=int(m1), c=int(m2), r_radius=int(length_minor_axis), c_radius=int(length_major_axis), orientation=theta)
# plt.plot(rr,cc)
plt.plot(mu[0], mu[1], '*k')

plt.contour(xg, yg, npdf)
plt.grid()

plt.tight_layout()
plt.show()

#the lines are at 90 degrees and hence verified that angles match that of the major and minor axis

#plotting conditional; varied rho
#as derived in class; conditional x2|x1 has cov matrix as C11- C12*C22^-1*C21 and mean as -(C22^-1)C12(x2-mu2) + mu1 
#but in 2d gaussian; C11= sig1^2, C12=C21= rho*sig1*sig2 and C22= sig2^2
#note C-ii refers to sigma-ii and 

range_of_rhos= [-0.99, -0.95, -0.5, 0, -0.5, 0.95, 0.99]
for rho in range_of_rhos:
#we need to fix x1 to get a fucntion in x2
    sig = np.array([[s1*s1, s1*s2*rho], [s1*s2*rho, s2*s2]])
    x_2= 6 #fixed value of x1
    mean_conditional= m1 + sig[0,1]/sig[1,1]*(x_2 - m2)
    cov_matrix_conditional=  sig[0,0] - (sig[0,1]*sig[1,0])*(1/(sig[1,1]))

    #this is a 1d gaussian
    pdf_conditional= scp.stats.norm.pdf(x1, loc = mean_conditional, scale = cov_matrix_conditional)
    pdf_marginal= scp.stats.norm.pdf(x2, loc = m2, scale = sig[1,1])
    npdf = scp.stats.multivariate_normal.pdf(pos, mean = mu, cov = sig)
    plt.plot(x1, pdf_conditional+7, label= "conditional")
    plt.plot(pdf_marginal,x2, label= "marginal")
    plt.contour(xg, yg, npdf)
    plt.title("plot of join and conditional for rho=" +str(rho))
    plt.legend()
    os.chdir("D:\\github\\Data-Assimilation-Course-Repo\\hw2\\plots\\")
    plt.savefig("joint_conditional_marginal_rho="+str(rho)+".png")
    plt.clf()

#its undefined when rho is 1 or -1
#when rho is 0, the normal distribution is as if it is completely independant of x1. that is normal(m2, sig2).
#rho=0 gives ellispe contours with axis parallel to the  x1 and x2 axis. this is when x1 is independant of x2
#marginal doesnt change with rho





