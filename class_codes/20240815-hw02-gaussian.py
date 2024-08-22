import numpy as np
import scipy as scp
import numpy.linalg as npla
import matplotlib.pyplot as plt

## "np = numpy"
## "scp = scipy"
## "npla" = "numpy.linalg"
## "plt" = "matplotlib.pyplot"
## etc.!!

# parameters needed to define a 2-dim Gaussian:
# means [m1, m2], std.dev. [s1, s2], and correlation [rho]
s1 = 1.0; s2 = 2.0; rho = 0.85; m1 = 1.7; m2 = 9.4
sig = np.array([[s1*s1, s1*s2*rho], [s1*s2*rho, s2*s2]])
mu = np.array([m1, m2])

# number of points creating a grid for plotting
npts = 30
x1 = np.linspace(m1 - 2.5*s1, m1 + 2.5*s1, npts)
x2 = np.linspace(m2 - 2.5*s2, m2 + 2.5*s2, npts)
xg, yg = np.meshgrid(x1, x2)
pos = np.dstack((xg, yg))

# compute the Gaussian density
npdf = scp.stats.multivariate_normal.pdf(pos, mean = mu, cov = sig)

plt.contour(xg, yg, npdf)


## eigen-values and -vectors of the covariance matrix
print(npla.eig(sig))
eval, evec = npla.eig(sig)
print(evec[0], evec[1])
print(evec[0][0], evec[0][1])


### plot the marginals as well
plt.contour(xg, yg, npdf)
plt.plot(mu[0], mu[1], '*k')
plt.grid()

plt.title(f'find the relation of semi-major/minor axis to eigenvectors\n{evec[0]} and {evec[1]}')

# some adjustment for getting the plot to "look" nice
plt.plot(x1, scp.stats.norm.pdf(x1, loc = mu[0], scale = s1)*5 + 6, 'c')
plt.plot(5*scp.stats.norm.pdf(x2, loc = mu[1], scale = s2), x2, 'm')

plt.tight_layout()


### plot the conditional as well

plt.contour(xg, yg, npdf)
plt.plot(mu[0], mu[1], '*k')
# plt.grid()
# plt.plot(mu[0] + evec[0][0]*(x1 - mu[0]), mu[1] + evec[0][1]*(x2 - mu[1]))
# plt.plot(x1, mu[1] + evec[0][1]/evec[0][0]*(x1 - mu[0]))

plt.title(f'two different conditional distributions,\nfor two different values of x2')

plt.plot(x1, scp.stats.norm.pdf(x1, loc = mu[0], scale = s1)*5 + 6, 'k')


yobs = 11.0
m1cond = m1 + sig[0,1]/sig[1,1]*(yobs - m2)
s1cond = sig[0,0] - sig[0,1]*sig[1,0]/sig[1,1]
plt.plot(x1, scp.stats.norm.pdf(x1, loc = m1cond, scale = s1cond)*5 + 6, 'c')

yobs = 8.0
m1cond = m1 + sig[0,1]/sig[1,1]*(yobs - m2)
s1cond = sig[0,0] - sig[0,1]*sig[1,0]/sig[1,1]
plt.plot(x1, scp.stats.norm.pdf(x1, loc = m1cond, scale = s1cond)*5 + 6, 'c')

plt.tight_layout()
plt.show()
