import matplotlib.pyplot as plt
plt.rcdefaults()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import math


def label(xy, text):
    y = xy[1] - 0.15  # shift y-value for label so that it's below the artist
    plt.text(xy[0], y, text, ha="center", family='sans-serif', size=14)

def create_plot(path,obstacle_enu,obstacle_radius,app_radius,wp_enu):


    fig, ax = plt.subplots()
    grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
    patches = []

    # add a circle

    circle = mpatches.Circle([obstacle_enu[0],obstacle_enu[1]], obstacle_radius, ec="none")
    patches.append(circle)

    circle2 = mpatches.Circle([obstacle_enu[0],obstacle_enu[1]], app_radius, ec="none")
    patches.append(circle2)
    # add a line
    path = np.array(path)
    x = path[:,0].tolist()
    x = [round(elem,2) for elem in x]
    y = path[:,1].tolist()
    y = [round(elem,2) for elem in y]
    plt.plot(x,y,'ro')
    e = wp_enu[0]
    o = wp_enu[1]
    plt.plot(e,o,'bo')

    x = 0
    y = 0
    plt.plot(x,y,'ro')

    colors = np.linspace(0, 1, len(patches))
    collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.axis('equal')
    plt.axis('off')

    plt.show()

def create_plot_multi(path,obstacles,safety_dist,wp_enu):


    fig, ax = plt.subplots()
    grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
    patches = []

    # add a circle
    for obstacle in obstacles:
        circle = mpatches.Circle([obstacle.enu[0],obstacle.enu[1]], obstacle.radius, ec="none")
        patches.append(circle)
        circle2 = mpatches.Circle([obstacle.enu[0],obstacle.enu[1]], obstacle.radius+safety_dist, ec="none")
        patches.append(circle2)
    # add a line
    path = np.array(path)
    x = path[:,0].tolist()
    x = [round(elem,2) for elem in x]
    y = path[:,1].tolist()
    y = [round(elem,2) for elem in y]
    plt.plot(x,y,'ro')
    e = wp_enu[0]
    o = wp_enu[1]
    plt.plot(e,o,'bo')

    x = 0
    y = 0
    plt.plot(x,y,'ro')

    colors = np.linspace(0, 1, len(patches))
    collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.axis('equal')
    plt.axis('off')

    plt.show()
