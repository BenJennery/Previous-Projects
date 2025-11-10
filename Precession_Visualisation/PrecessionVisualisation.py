import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 1         # gravitational constant
M = 10        # mass of the central body
dt = 0.005    # time step
radius = 0.6  # radius of star

starr = [np.array([0.0, 0.0])]
r1 = np.array([2.0, 0.0])
v1 = np.array([0.0, 2.2])
r2 = np.array([2.0, 0.0])
v2 = np.array([0.0, 2.2])
xs1, ys1 = [], []
xs2, ys2 = [], []
xss, yss = [0,0], [0,0]

for i in range (0,6) :
    starr.append(np.array([radius*np.sin((i*np.pi)/3) ,radius*np.cos((i*np.pi)/3)]))
    xss.append(radius*np.sin((i*np.pi)/3))
    yss.append(radius*np.cos((i*np.pi)/3))

fig, (fig1, fig2, fig3) = plt.subplots(3, 1, figsize=(8, 8))
fig1.set_aspect('equal')
fig1.set_xlim(-3, 3)
fig1.set_ylim(-3, 3)
star, = fig1.plot(0, 0, 'go', markersize=25)
#planet1, = fig1.plot([], [], 'bo', markersize=6)
planet2, = fig1.plot([], [], 'ro', markersize=6)
#trail1, = fig1.plot([], [], 'b-', lw=1)
trail2, = fig1.plot([], [], 'r-', lw=1)
starmass = fig1.plot([xss] ,[yss], 'ro', markersize=3)

fig1.set_xlabel("   ")

#fig2.set_title("Acceleration for both planets")
fig2.set_ylabel("Magnitude")
line_diff, = fig2.plot([], [], 'r-', lw=1)
line_diff2, = fig2.plot([], [], 'g-', lw=1)

fig3.set_xlabel("Frame")
fig3.set_ylabel("Magnitude diff")
line_diff3, = fig3.plot([], [], 'r-', lw=1)

diff_magnitudes = []
difff_magnitudes = []
aprox_magnitudes = []
frames_list = []

def update(frame):
    global r1, v1, r2, v2
    
    dist1 = np.linalg.norm(r1)
    a1 = -G * M * r1 / dist1**3
    a2 = [0.0, 0.0]
    a22 = -(G * M * r2 / (np.linalg.norm(r2))**3)
    for i in range (0,7) :
        a2 += -G * (M/7) * (-starr[i]+r2) / ((np.linalg.norm(-starr[i]+r2))**3)

    v1 += a1 * dt
    r1 += v1 * dt
    v2 += a2 * dt
    r2 += v2 * dt
    
    xs1.append(r1[0])
    ys1.append(r1[1])
    xs2.append(r2[0])
    ys2.append(r2[1])
    diff_vec = a2 
    diff_magnitudes.append(np.linalg.norm(diff_vec))
    diff_vecc = a2 + (G * M * r2 / (np.linalg.norm(r2))**3)
    difff_magnitudes.append(np.linalg.norm(diff_vecc))
    aprox_magnitudes.append(np.linalg.norm(a22))
    frames_list.append(frame)

    #planet1.set_data([r1[0]], [r1[1]])
    #trail1.set_data(xs1, ys1)
    
    planet2.set_data([r2[0]], [r2[1]])
    trail2.set_data(xs2, ys2)
    
    line_diff.set_data(frames_list, diff_magnitudes)
    line_diff2.set_data(frames_list, aprox_magnitudes)
    fig2.set_xlim(0, frame)
    fig2.set_ylim(0, max(0.1, np.max(diff_magnitudes)*1.1))
    
    line_diff3.set_data(frames_list, difff_magnitudes)
    fig3.set_xlim(0, frame)
    fig3.set_ylim(0, max(0.1, np.max(difff_magnitudes)*1.1))
    
    return planet2, trail2, line_diff, line_diff2, line_diff3 #, planet1 , trail1

ani = FuncAnimation(fig, update, frames=1000000, interval=5, blit=True)
plt.show()