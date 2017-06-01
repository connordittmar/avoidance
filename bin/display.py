
import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import BoxStyle

NUM = 250

object = Ellipse(x=0,y=0, width=1, height=1, angle=rnd.rand()*360)

fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(rnd.rand())
    e.set_facecolor(rnd.rand(3))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()

# Generate Path Graphics
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Plotted Path')
plt.grid(True)
plt.savefig("test.png")
plt.show()
