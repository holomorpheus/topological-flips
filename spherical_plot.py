"""
Spherical Skate Trick Plot

Current version: Jul 26 2024
Created: Jul 19 2021

Author: Gabriel Martins (@holomorpheus)
Contributor: Justus Carlisle
"""

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import os

from numpy import cos, sin, pi

# Local imports
import flip_plotting_functions as FPF
import homotopy_plotting_functions as HPF
import name_functions as NF

def generate_axis():
    
    fig = plt.figure(figsize=(8, 8))
    
    # Define axis
    ax = fig.add_subplot(1,1,1,projection='3d')
    
    scope = 1.
    ax.set_xlim([-scope,scope])
    ax.set_ylim([-scope,scope])
    ax.set_zlim([-scope,scope])
    ax.set_box_aspect((1,1,1))
    ax.azim = 35
    ax.elev = 13
    
    # Determining gridlines
    tscope = .8*scope
    ticks = [-tscope+k*tscope/2 for k in range(5)]
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.set_ticks(ticks)
        axis.set_ticklabels([])
        axis._axinfo['tick']['inward_factor'] = 0.
        axis._axinfo['tick']['outward_factor'] = 0.
        
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        
    return fig, ax

def sphere_surface_plot(ax):
    
    if ax is None:
        
        ax = generate_axis()
        
    # Define sphere parametrization
    pphi, ttheta = np.mgrid[0.0:pi:100j, 0.0:2.0*pi:100j]
    xx = sin(pphi)*cos(ttheta)
    yy = sin(pphi)*sin(ttheta)
    zz = cos(pphi)
    
    # Plot sphere
    ax.plot_surface( xx, yy, zz, color='g', alpha=0.25, zorder=1)
    
def sphere_flip_plot(name, Npoints = 100, save = False, dirname = 'images'):
    
    fig, ax = generate_axis()    
    sphere_surface_plot(ax)
    
    # Plot curve    
    curve = FPF.ndarray_spherical_flip(name, Npoints)
    x, y, z = curve[0,:], curve[1,:], curve[2,:]
    
    ax.plot( x, y, z, color='k', linewidth=3, zorder=3)
    
    ax.scatter( x[0], y[0], z[0], s=60, color='k', zorder=3)
    ax.scatter( x[-1], y[-1], z[-1], s=60, color='k', zorder=3)
    
    if save:
        
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        
        if not os.path.exists(dirname):
            os.mkdir(dirname)
            
        filename = NF.trick_handle(name)
        filestring = dirname+'/'+filename
        fig.savefig(filestring)
        
def sphere_homotopy_plot(trick_pair, steps = 12, Npoints = 201,
                  nonlinear_s=None, save = False, dirname = 'images'):
    
    reduced_pair = NF.reduce_deformation(trick_pair)
    
    fig, ax = generate_axis()    
    sphere_surface_plot(ax)
    
    # Plot curves    
    curves = HPF.ndarray_spherical_homotopy(reduced_pair, Npoints, steps,
                                            nonlinear_s=nonlinear_s)
            
    for i in range(steps):
        x, y, z = curves[0,i,:], curves[1,i,:], curves[2,i,:]
                      
        if i == 0:
            ax.plot( x, y, z, color='darkmagenta', linewidth=3, zorder=4)
        
        elif i == steps-1:
            ax.plot( x, y, z, color='navy', linewidth=3, zorder=4)
            
            ax.scatter( x[0], y[0], z[0], s=60, color='k', zorder=4)
            ax.scatter( x[-1], y[-1], z[-1], s=60, color='k', zorder=4)
            
        else:
            ax.plot( x, y, z, color='k', alpha=1., linewidth=2, zorder=3)
            
        if save:
            
            if not os.path.exists(dirname):
                os.mkdir(dirname)
                
            filename = NF.deformation_handle(reduced_pair)
            filestring = dirname+'/'+filename
            fig.savefig(filestring)
            