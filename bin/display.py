
import matplotlib.pyplot as plt
import numpy.random as rnd
from matplotlib.patches import BoxStyle

NUM = 250

object = BoxStyle.Circle(pad=0.2)

fig = plt.figure(0)
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

plt.show()


t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Plotted Path')
plt.grid(True)
plt.savefig("test.png")
plt.show()
