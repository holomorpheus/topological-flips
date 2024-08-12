"""
Fliptrick Animation

Current version: Jul 25 2024
Created: Aug 10 2021

Author:
    Gabriel Martins
"""

import matplotlib.animation as animation
import os

import skate_plot as SP
import flip_plotting_functions as FPF
import name_functions as NF
    
def animate_fliptrick(name, title = None, Nframes = 30, margin_frames = 12,
            grid_points = 241, save = True, fps = 24, dirname = "videos", 
            filename = None, fancy = True, pop = True):
    
    total_frames = Nframes + 2*margin_frames
    name = NF.clean_name(name)
    
    if title is None:
        title = NF.trick_title(name)
        
    if filename is None:
        filename = name+".mp4"
    
    # Create skate curve
    skatecurve = SP.skate_curve(grid_points=grid_points)
        
    if fancy:
        R = FPF.fancy_ndarray_rotation_flip(name, Nframes, margin_frames)
    else:
        R = FPF.ndarray_rotation_flip(name, Nframes, margin_frames)
    
    if pop:
        vt = FPF.vertical_translation( Nframes = Nframes,
                                   margin_frames = margin_frames,
                                   grid_points=grid_points)
    
    # Create figure and axis
    fig, ax = SP.generate_axis(title=title)
    
    # Animation update function.
    if pop:
        
        def update(i):
            for line in ax.get_lines():
                line.remove()
            SP.plot(R[:,:,i]@skatecurve + vt[:,:,i], ax=ax)
            
    else:
        
        def update(i):
            for line in ax.get_lines():
                line.remove()
            SP.plot(R[:,:,i]@skatecurve, ax=ax)
    
    # Call the animator.  blit=True means only re-draw the parts that have changed.
    ani = animation.FuncAnimation(fig, update, total_frames)
    
    # Save animation
    if save:
        
        if not os.path.exists(dirname):
            os.mkdir(dirname)
            
        writer=animation.FFMpegWriter(fps=fps)
        ani.save(dirname+"/"+filename, writer=writer,dpi=200)
    
    
    
    
    