"""
Homotopy Animations

Current version: July 23rd 2024
Created: March 4th 2021

Author: Gabriel Martins
"""

# Libraries
import matplotlib.animation as animation
import os

# Local Modules
import skate_plot as SP
import homotopy_plotting_functions as HPF
import name_functions as NF

# Animation function
def animate_homotopy( trick_pair, title = None, steps = 16, step_frames = 30,
        rest_frames = 6, margin_frames = 12, grid_points = 241, pop = True,
        save = True, fps = 24, dirname = "videos", filename = None,
        nonlinear_s=None, fancy = True):
    
    total_frames = 2*margin_frames
    total_frames += steps*(step_frames+rest_frames)  + rest_frames
    
    flip1, flip2 = NF.reduce_name(trick_pair[0]), NF.reduce_name(trick_pair[1])
    trick_pair = (flip1, flip2)
    
    if title is None:
        title = NF.deformation_title(trick_pair)
        
    if filename is None:
        filename = NF.deformation_handle(trick_pair)+".mp4"
    
    # Create skate curve
    skatecurve = SP.skate_curve(grid_points=grid_points)
    
    # Define homotopy    
    if fancy:
        R = HPF.fancy_ndarray_rotation_homotopy(trick_pair, steps, step_frames,
                        rest_frames, margin_frames, nonlinear_s=nonlinear_s)
    else: 
        R = HPF.ndarray_rotation_homotopy(trick_pair, steps, step_frames,
                                          rest_frames, margin_frames,
                                          nonlinear_s=nonlinear_s)
    
    # Vertical movement array
    if pop:
        vt = HPF.vertical_translation_homotopy( steps = steps,
                     step_frames = step_frames, rest_frames = rest_frames,
                     margin_frames = margin_frames, grid_points = grid_points)
    
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
    if save == True:
        
        if not os.path.exists(dirname):
            os.mkdir(dirname)
            
        writer=animation.FFMpegWriter(fps=fps)
        ani.save(dirname+"/"+filename, writer=writer,dpi=200)
