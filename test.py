import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def update_points(num):
    '''
    更新数据点
    '''
    point_ani.set_data(x[num], y[num])
    return point_ani,

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig = plt.figure(tight_layout=True)
plt.plot(x, y)
print('show the picture.')
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
# 开始制作动画
ani = animation.FuncAnimation(fig, update_points, np.arange(0, 200), interval=50, blit=True)
# ani.save('sin_test2.gif', writer='imagemagick', fps=10)
plt.show()
