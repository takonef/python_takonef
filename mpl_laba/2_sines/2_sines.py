import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

with open('frames.dat', 'r') as f:
    lines = f.readlines()

frames = []
for i in range(0, len(lines), 2):
    x = np.array([float(j) for j in lines[i].split()])
    y = np.array([float(j) for j in lines[i+1].split()])
    frames.append((x, y))

all_x = np.concatenate([f[0] for f in frames]) # чтб границы не воландались
all_y = np.concatenate([f[1] for f in frames])
x_min, x_max = np.min(all_x), np.max(all_x)
y_min, y_max = np.min(all_y), np.max(all_y)

x_pad = (x_max - x_min) * 0.05
y_pad = (y_max - y_min) * 0.05    
x_limits = (x_min - x_pad, x_max + x_pad)
y_limits = (y_min - y_pad, y_max + y_pad)


fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
line, = ax.plot([], [], linewidth=2)

ax.set_xlim(x_limits)
ax.set_ylim(y_limits)
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth=0.7, color='gray')
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray')

ax.set_xlabel('X')
ax.set_ylabel('Y')
def update(idx):
    idx = idx - 2*(idx%5)*((idx-1)//5) # клянусь оно работает,, можно было бы писать не 5, а len(frames) - 1, но это было бы совсем страшно
    x, y = frames[idx]
    line.set_data(x, y)
    ax.set_title(f"Frame {idx}", fontsize=14)
    return line, ax

anim = ani.FuncAnimation(
    fig,
    update,
    frames=10,
    interval=200, # мс, но это только для отображения пока программа идет, где сохраняется будут кадры в секунду
    repeat=True
)

writer = ani.PillowWriter(fps=6)
anim.save('frames_animation.gif', writer=writer)

plt.show()