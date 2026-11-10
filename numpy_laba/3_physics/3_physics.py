import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

with open('start.dat', 'r') as f:
    text = f.read()
u = np.array([float(j) for j in text.split()])

N = 255
history = [u]
for _ in range(N):
    Au = u - np.roll(u, 1)
    u = u - 0.5 * Au
    history.append(u)

fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
line, = ax.plot([], [], linewidth=2)

y_min, y_max = np.min(history), np.max(history)
y_pad = (y_max - y_min) * 0.05
ax.set_ylim(y_min - y_pad, y_max + y_pad)
ax.set_xlim(0, len(u) - 1)

ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth=0.7, color='gray')
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray')
ax.set_xlabel('idx')
ax.set_ylabel('u[idx]')

def update(idx):
    cur = history[idx]
    line.set_data(np.arange(len(cur)), cur)
    ax.set_title(f"Step {idx}", fontsize=14)
    return line, ax

anim = ani.FuncAnimation(
    fig,
    update,
    frames=len(history),
    interval=30, # мс
    repeat=True
)

writer = ani.PillowWriter(fps=30)
anim.save('3_physics.gif', writer=writer)

plt.show()