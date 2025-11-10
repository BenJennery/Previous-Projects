import matplotlib.pyplot as plt
import numpy as np

a = 10
b = 2.6
c = 28

dt = 0.01

dx = 0
dy = 0
dz = 0
x = 0
y = 1
z = 1.1
arrayx = []
arrayy = []
arrayz = []
for i in range (0,20000) :
    dx = a*(y-x)
    dy = x*(c-z)-y
    dz = x*y-b*z
    x += dx * dt
    y += dy * dt
    z += dz * dt
    arrayx.append(x)
    arrayy.append(y)
    arrayz.append(z)

plt.style.use('dark_background')
ax = plt.figure().add_subplot(projection='3d')
ax.plot(arrayx,arrayy,arrayz , lw=0.4 , color = "white" )
ax.set_axis_off()
plt.show()