"""
Fliptrick Plotting Functions

Current version: Aug 11 2024
Created: Apr 21 2021

Author: Gabriel Martins (@holomorpheus)
"""

# Libraries
import numpy as np
import sympy as sm

# Local imports
from flip_list import t
from flip_list import symbolic_rotation_flip
from flip_list import symbolic_quaternion_flip
from fancy_plotting import pop_rotation

# Flip animation functions
def ndarray_rotation_flip(name, Nframes, margin_frames, tmax=1):
    
    symb_flip = symbolic_rotation_flip(name)
    funcflip = sm.lambdify(t, symb_flip, "numpy")
    
    total_frames = Nframes + 2*margin_frames
    R = np.zeros((3,3,total_frames))
    
    dt = tmax/(Nframes-1)
    
    for i in range(margin_frames):
        R[:,:,i] = np.eye(3)
        Rend = funcflip(1.)
        R[:,:,-1-i] = Rend
        
    for i in range(Nframes):
        Ri = funcflip(i*dt)
        R[:,:,margin_frames+i] = Ri
    
    return R

def fancy_ndarray_rotation_flip(name, Nframes, margin_frames, tmax=1):
    
    from numpy import pi, sin
    
    symb_flip = symbolic_rotation_flip(name)
    funcflip = sm.lambdify(t,symb_flip,"numpy")
    
    total_frames = Nframes + 2*margin_frames  
    
    R = np.zeros((3,3,total_frames))
    
    Kframes = int(Nframes/16)
    Mframes = Nframes - 4*Kframes
    dt = 1/(Mframes-1)
    
    # Pop rotation
    A = pop_rotation(Nframes)
    
    Rend = funcflip(1.)
    
    for i in range(margin_frames):
        R[:,:,i] = np.eye(3)
        R[:,:,-1-i] = Rend
        
    for i in range(Nframes):
        
        if i < 3*Kframes:
            ti = 0
        elif i > 3*Kframes+Mframes:
            ti = tmax
        else:
            ti = sin((i-3*Kframes)*dt*pi/2)*tmax
            
        Ri = funcflip(ti)
        R[:,:,margin_frames+i] = A[:,:,i]@Ri
    
    return R

def vertical_translation(Nframes = 60, margin_frames = 12, grid_points = 241):
    
    total_frames = Nframes + 2*margin_frames
    
    t = np.linspace( 0, 1, Nframes)
    z = np.zeros(total_frames)
    z[margin_frames:Nframes+margin_frames] = 10*t*(1-t)
    
    vt = np.zeros(( 3, grid_points, total_frames))
    
    for j in range(grid_points):
        vt[2,j,:] = z
    
    return vt

# Spherical plot
def ndarray_spherical_flip(name, Npoints):
    
    from numpy.linalg import norm
    
    q = symbolic_quaternion_flip(name)
    q = q.to_Matrix()    
    q.simplify()    
    sq = sm.Matrix([q[0],-q[1],-q[3]])
    
    fsq = sm.lambdify(t,sq,"numpy")
    curve = np.zeros((3,Npoints))
    
    nt = np.linspace(0,1,Npoints)
        
    for i in range(Npoints):
        
        ct = fsq(nt[i])[:,0]
        curve[:,i] = ct/norm(ct)
    
    return curve