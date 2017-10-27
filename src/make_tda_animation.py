"""
This script makes random data and animation.

"""

import numpy as np
import scipy.spatial.distance as dist
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sacred import Experiment

ex = Experiment('tda')

def plot(frame, fig, x, y, xy, dmat):
    nsample = len(x)
    plt.cla()
    ax = fig.add_subplot(111)
    r = 0.002*frame
    for i, j in zip(x, y):
        c = plt.Circle((i, j), r, color='r', alpha=0.1)
        ax.add_artist(c)
    for i in range(nsample):
        for j in range(nsample):
            if dmat[i, j] / 2 < r:
                _xy = np.stack((xy[i, :], xy[j, :]))
                _x = _xy[:, 0]
                _y = _xy[:, 1]                
                ax.plot(_x, _y, c='b', alpha=0.2)
                
    ax.axis('equal')    
    ax.set_xlim([-0.2, 1.3])
    ax.set_ylim([-0.5, 1.5])

@ex.config
def config():
    datatype = 'random'
    assert datatype in ['random', 'circle'], f"Not implement {datatype}"
    seed = 4 
    nsample = 100
    scale = 0.2
    output_filename = ""
    
@ex.capture
def random(seed, nsample):
    np.random.seed(seed)
    xy = np.random.random((nsample, 2))
    fig = plt.figure()
    x = xy[:,0]
    y = xy[:,1]
    dmat = dist.cdist(xy, xy)
    fargs = [fig, x, y, xy, dmat]
    ani = animation.FuncAnimation(fig, plot, frames=range(100), fargs=fargs, interval=100)
    ani.save("random.mpeg")

@ex.capture    
def circle(seed, nsample, scale):
    np.random.seed(seed+1)
    fig = plt.figure()
    theta = np.linspace(0, 2*np.pi, nsample)
    a, b = 1 * np.cos(theta), 1 * np.sin(theta)
    r = np.random.uniform(0.5, 1.0, size=nsample)
    x, y = r * np.cos(theta) + 0.5 , r * np.sin(theta) + 0.5
    xy = np.vstack([x,y]).T
    dmat = dist.cdist(xy, xy)
    fargs = [fig, x, y, xy, dmat]
    ani = animation.FuncAnimation(fig, plot, frames=range(100), fargs=fargs, interval=100)
    ani.save("circle.mpeg")

@ex.command
def example(seed):
    fig = plt.figure(dpi=70)    
    ax = fig.add_subplot(111)
    np.random.seed(seed)
    xy = np.random.random((5, 2))
    nsample = 5
    x = xy[:,0]
    y = xy[:,1]
    dmat = dist.cdist(xy, xy)
    r = 0.1
    seq = 'abcde'
    for i in range(nsample):
        c = plt.Circle((x[i], y[i]), r, color='r', alpha=0.4)
        ax.add_artist(c)            
        for j in range(i, nsample):        
            if dmat[i, j] / 2 < r:
                _xy = np.stack((xy[i, :], xy[j, :]))
                _x = _xy[:, 0]
                _y = _xy[:, 1]                
                ax.plot(_x, _y, c='b', alpha=0.5, linewidth=5)
        plt.text(x[i], y[i]-0.02, seq[i], ha='center', fontsize=25)                
    ax.axis('equal')    
    ax.set_xlim([-0.2, 1.3])
    ax.set_ylim([-0.5, 1.5])
    plt.savefig(f'example_{r}.png')
    plt.show()

@ex.automain
def main(datatype):
    if datatype == 'random':
        random()
    elif datatype == 'circle':
        circle()
