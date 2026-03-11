import numpy as np
import matplotlib.pyplot as plt

nx = 41
ny = 41
nt = 500

dx = 2/(nx-1)
dy = 2/(ny-1)

rho = 1
nu = 0.1
dt = 0.001

u = np.zeros((ny,nx))
v = np.zeros((ny,nx))
p = np.zeros((ny,nx))
b = np.zeros((ny,nx))

def pressure_poisson(p,dx,dy,b):

    pn = np.empty_like(p)

    for q in range(50):

        pn = p.copy()

        p[1:-1,1:-1] = (
        ((pn[1:-1,2:] + pn[1:-1,0:-2])*dy**2 +
        (pn[2:,1:-1] + pn[0:-2,1:-1])*dx**2)
        /(2*(dx**2 + dy**2))
        - dx**2*dy**2/(2*(dx**2 + dy**2))*b[1:-1,1:-1]
        )

        p[:,-1] = p[:,-2]
        p[:,0] = p[:,1]
        p[0,:] = p[1,:]
        p[-1,:] = 0

    return p

for n in range(nt):

    un = u.copy()
    vn = v.copy()

    b[1:-1,1:-1] = (
        rho*(1/dt*((un[1:-1,2:]-un[1:-1,0:-2])/(2*dx) +
        (vn[2:,1:-1]-vn[0:-2,1:-1])/(2*dy)))
    )

    p = pressure_poisson(p,dx,dy,b)
    u[1:-1,1:-1] = (
    un[1:-1,1:-1]
    - un[1:-1,1:-1]*dt/dx*(un[1:-1,1:-1]-un[1:-1,0:-2])
    - vn[1:-1,1:-1]*dt/dy*(un[1:-1,1:-1]-un[0:-2,1:-1])
    - dt/(2*rho*dx)*(p[1:-1,2:]-p[1:-1,0:-2])
    + nu*(dt/dx**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])
    + dt/dy**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1]))
    )
    v[1:-1,1:-1] = (
    vn[1:-1,1:-1]
    - un[1:-1,1:-1]*dt/dx*(vn[1:-1,1:-1]-vn[1:-1,0:-2])
    - vn[1:-1,1:-1]*dt/dy*(vn[1:-1,1:-1]-vn[0:-2,1:-1])
    - dt/(2*rho*dy)*(p[2:,1:-1]-p[0:-2,1:-1])
    + nu*(dt/dx**2*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2])
    + dt/dy**2*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[0:-2,1:-1]))
    )
    # Boundary conditions
    u[0,:] = 0
    u[:,0] = 0
    u[:,-1] = 0
    u[-1,:] = 1

    v[0,:] = 0
    v[-1,:] = 0
    v[:,0] = 0
    v[:,-1] = 0

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

X,Y = np.meshgrid(x,y)
# Streamlines
plt.figure(figsize=(7,7))
plt.streamplot(X,Y,u,v,density=2)
plt.title("Lid Driven Cavity Flow")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
# Velocity vectors
plt.figure(figsize=(7,7))
plt.quiver(X,Y,u,v)
plt.title("Velocity Field")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.figure(figsize=(6,6))
plt.streamplot(X,Y,u,v)
plt.show()

