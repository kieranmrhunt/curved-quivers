import matplotlib.pyplot as plt
import numpy as np
from modplot import velovect

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]

#U = -1 - X**2 + Y
#V = 1 + X - Y**2

#U = np.sin(X)*np.sin(Y)
#V = np.cos(X)*np.sin(Y)

U = -Y
V = X

#U = -Y*np.sin(Y)*np.cos(Y)
#V = X*np.sin(X)*np.cos(X)


W = np.sqrt(U**2 + V**2)

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,4))

s=10
ax1.quiver(X[::s,::s],Y[::s,::s],U[::s,::s],V[::s,::s])
ax2.streamplot(X,Y,U,V, color='k')


grains = 15
tmp =  np.linspace(-3, 3, grains)
xs = np.tile(tmp, grains)
ys = np.repeat(tmp, grains)


seed_points = np.array([list(xs), list(ys)])

scale=2.

velovect(ax3,X,Y,U,V, arrowstyle='fancy', scale = 1.5, grains = 15, color='k')

				   
for ax in ax1, ax2, ax3:
	cs = ax.contourf(X,Y, W, cmap=plt.cm.viridis, alpha=0.5, zorder=-1)
	ax.set_xlim([-3,3])
	ax.set_ylim([-3,3])

ax1.set_title("Quiver")
ax2.set_title("Streamplot")
ax3.set_title("Curved quivers")


plt.colorbar(cs, ax=[ax1,ax2,ax3])    
plt.show()


