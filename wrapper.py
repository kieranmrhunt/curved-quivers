import matplotlib.pyplot as plt
import numpy as np
from modplot import velovect

w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]

#U = -1 - X**2 + Y
#V = 1 + X - Y**2

U = np.sin(X)*np.sin(Y)
V = np.cos(X)*np.sin(Y)

W = np.sqrt(U**2 + Y**2)

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))

s=10
ax1.quiver(X[::s,::s],Y[::s,::s],U[::s,::s],V[::s,::s])
ax2.streamplot(X,Y,U,V, color='k')


grains = 12
tmp = tuple([x]*grains for x in np.linspace(-3, 3, grains))
xs = []
for x in tmp:
    xs += x
ys = tuple(np.linspace(-3, 3, grains))*grains


seed_points = np.array([list(xs), list(ys)])

scale=2.

splot(ax3,X,Y,U,V, arrowstyle='fancy', integration_direction='forward', density=10,
                   minlength=.9*scale/grains, maxlength = scale/grains, start_points = seed_points.T,
				   color='k')

				   
for ax in ax1, ax2, ax3:
	ax.pcolormesh(X,Y, W, cmap=plt.cm.viridis, alpha=0.5, zorder=-1)

    
plt.show()


