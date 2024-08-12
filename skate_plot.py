"""
Skate Plot

Current version: Jul 25 2024
Created: Aug 10 2021

Author:
    Gabriel Martins
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from numpy import cos, pi

def yz_function(x, lx, ly):
    
    N, = x.shape
    
    y = np.zeros(N)
    z = np.zeros(N)
    lx2, ly2 = lx/2, ly/2
    
    for i in range(N):
        
        if x[i] < lx2 - 1:
            y[i] = ly2
        else:
            s = lx2-x[i]
            y[i] = ly2*np.sqrt(1-(1-s)**2)
            z[i] = ly2*(.7*(1-s))**2
    
    return (y,z)
    
def skate_curve(length = 6, width = 1.5, grid_points = 241):
        
    lx, ly = length, width
    
    quarter_grid_points = grid_points//4 + 1
    half_grid_points = 2*quarter_grid_points - 1
    grid_points = 2*half_grid_points - 1
    
    if grid_points % 4 != 1:
        print('\n------------------------------')
        print("From skate_curve function:")
        print("The value of grid_points was modified.")
        print("Current value: grid_points =", grid_points)
        print('------------------------------\n')
        
    skate_points = np.zeros(( 3, grid_points))
    
    tenth_grid_points = half_grid_points//5
    s = np.linspace( pi/2, 0, tenth_grid_points)
    nose = cos(s) + lx/2 - 1
    
    
    flat_grid_points = quarter_grid_points - tenth_grid_points + 1
    s = np.linspace( 0, lx/2 - 1, flat_grid_points)
    xq = np.concatenate(( s[:-1], nose))
    yq, zq = yz_function(xq, lx, ly)

    xh = np.concatenate(( -np.flip(xq), xq[1:]))
    yh = np.concatenate((  np.flip(yq), yq[1:]))
    zh = np.concatenate((  np.flip(zq), zq[1:]))
    
    x0, y0, z0 = np.array([xh[0]]), np.array([yh[0]]), np.array([zh[0]])
    
    # Skate Curve
    skate_points[0,:] = np.concatenate(( xh[:-1],  np.flip(xh)[:-1], x0))
    skate_points[1,:] = np.concatenate(( yh[:-1], -np.flip(yh)[:-1], y0))
    skate_points[2,:] = np.concatenate(( zh[:-1],  np.flip(zh)[:-1], z0))
    
    return skate_points

def generate_axis(scope = None, title = None):
    
    if scope is None:
        scope = 3.2
        
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection='3d')
    
    ax.set_xlim([-scope,scope])
    ax.set_ylim([-scope,scope])
    ax.set_zlim([-scope,scope])
    ax.set_box_aspect((1,1,1))
    ax.azim = -135
    
    # Create initial static frames
    tscope = .8*scope
    ticks = [-tscope+k*tscope/2 for k in range(5)]
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.set_ticks(ticks)
        axis.set_ticklabels([])
        axis._axinfo['tick']['inward_factor'] = 0.0
        axis._axinfo['tick']['outward_factor'] = 0.0
        
    if title is not None:
        ax.set_title(title)
        
    return fig, ax

def plot(curve, ax=None, colormap='inferno'):
    
    if ax is None:
        fig, ax = generate_axis()
    
    # Relevant gridpoint sizes
    N = curve.shape[1]
    M = (N-1)//2 + 1
    L = (M-5)//2 + 1
    K = (L-1)//2 + 1
    
    # Get colormap
    cmap = cm.get_cmap(colormap, L)
    
    # Define colors along skateboard
    s = .5*(np.linspace( 0, 1, K)**(1.5))
    s = np.concatenate((-np.flip(s)[:-1],s))+.5
    colors = cmap(s)
    
    # Create list of line elements
    lines = (L+1)*[0]
    
    for i in range(L):
        
        k = 2*i+2
        
        x = [ curve[0,k], curve[0,N-k-1]]
        y = [ curve[1,k], curve[1,N-k-1]]
        z = [ curve[2,k], curve[2,N-k-1]]
        
        lines[i+1], = ax.plot(x,y,z,color=colors[i])
        
    lines[0], = ax.plot( curve[0,:], curve[1,:], curve[2,:], color='k', zorder=2)
    
    return [ax, lines]
    