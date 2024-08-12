"""
Spherical Homotopies

Current version Aug 11 2024
Created Jul 25 2024

Author: Gabriel Martins (@holomorpheus)
"""

# Libraries
import sympy as sm
import numpy as np

from numpy import pi, sin

# Local imports
from homotopy_list import symbolic_spherical_homotopy
from homotopy_list import symbolic_rotation_homotopy
from homotopy_list import s, t
from fancy_plotting import pop_rotation

homotopies_nonlinear_s = {
    ('kickflip','heelflip'): False,
    ('heelflip','kickflip'): False,
    ('360shoveit','fs360shoveit'): False,
    ('fs360shoveit','360shoveit'): False,
    ('kickflip','360shoveit'): False,
    ('360shoveit','kickflip'): False,
    ('heelflip','360shoveit'): False,
    ('360shoveit','heelflip'): False,
    ('varialflip','540shoveit'): False,
    ('540shoveit','varialflip'): False,
    ('varialflip','inwardheelflip'): False,
    ('inwardheelflip','varialflip'): False,
    ('hardflip','varialheelflip'): False,
    ('varialheelflip','hardflip'): False,
    ('ollie','doublekickflip'): True,
    ('doublekickflip','ollie'): True,
    ('shoveit','varialdoubleflip'): True,
    ('varialdoubleflip','shoveit'): True,
    ('wobbling360shoveit','360shoveit') : False,
    ('wobblingkickflip','kickflip') : False,
    ('hardflip','muskahardflip') : True,
    ('muskahardflip','hardflip') : True}

# Animation functions
def ndarray_rotation_homotopy(reduced_pair, steps, step_frames,
                              rest_frames, margin_frames, nonlinear_s=None,
                              tmax=1 ):
    
    symb_homotopy = symbolic_rotation_homotopy(reduced_pair)
    fhomo = sm.lambdify((s,t), symb_homotopy, "numpy")
    
    if rest_frames % 2 == 1:
        rest_frames += 1
    
    total_frames = steps*(step_frames+rest_frames) + rest_frames
    total_frames += 2*margin_frames
    
    dt = tmax/(step_frames-1)
    
    if nonlinear_s is None:
        nonlinear_s = homotopies_nonlinear_s[reduced_pair]
        
    if nonlinear_s:
        ns = (sin(np.linspace(-pi/2,pi/2,steps))+1)/2
    else:
        ns = np.linspace(0,1,steps)
    
    R = np.zeros((3,3,total_frames))
    
    Rend = fhomo(1., 1.)
    
    for i in range(margin_frames):
        R[:,:,i] = np.eye(3)
        R[:,:,-1-i] = Rend
        
    for j in range(rest_frames):
        R[:,:,margin_frames+j] = np.eye(3)
        R[:,:,total_frames-rest_frames-margin_frames+j] = Rend
        
    for i in range(1,steps):
        for j in range(rest_frames//2):
            k = margin_frames + i*(step_frames+rest_frames)
            R[:,:,k+j] = Rend
            R[:,:,k+rest_frames//2+j] = np.eye(3)
    
    for i in range(steps):
        for j in range(step_frames):
            
            ij = margin_frames + rest_frames + i*(step_frames+rest_frames) + j
            si, tj = np.float64((ns[i], j*dt))
    
            Rij = fhomo(si,tj)
            R[:,:,ij] = Rij
    
    return R

def fancy_ndarray_rotation_homotopy(reduced_pair, steps, dyn_frames,
                                    rest_frames, margin_frames,
                                    nonlinear_s=None, tmax=1. ):
    
    symb_homotopy = symbolic_rotation_homotopy(reduced_pair)
    fhomo = sm.lambdify((s,t), symb_homotopy, "numpy")
    
    if rest_frames % 2 == 1:
        rest_frames += 1
    
    total_frames = steps*(dyn_frames+rest_frames) + rest_frames
    total_frames += 2*margin_frames
    
    # Fancy frames
    Kdyn_frames = int(dyn_frames/16)
    Mdyn_frames = dyn_frames - 4*Kdyn_frames
    
    # Rotation about the x-axis
    A = pop_rotation(dyn_frames)
    
    dt = 1/(Mdyn_frames-1)
    
    if nonlinear_s is None:
        nonlinear_s = homotopies_nonlinear_s[reduced_pair]
        
    if nonlinear_s:
        ns = (sin(np.linspace(-pi/2,pi/2,steps))+1)/2
    else:
        ns = np.linspace(0,1,steps)
    
    Rend = fhomo( 1., 1.)
    R = np.zeros((3,3,total_frames))
    
    for i in range(margin_frames):
        R[:,:,i] = np.eye(3)    
        R[:,:,-1-i] = Rend
        
    for j in range(rest_frames):
        R[:,:,margin_frames+j] = np.eye(3)
        R[:,:,total_frames-rest_frames-margin_frames+j] = Rend
        
    for i in range(1,steps):
        for j in range(rest_frames//2):
            k = margin_frames + i*(dyn_frames+rest_frames)
            R[:,:,k+j] = Rend
            R[:,:,k+rest_frames//2+j] = np.eye(3)
    
    for i in range(steps):
        for j in range(dyn_frames):
            
            ij = margin_frames + rest_frames + i*(dyn_frames+rest_frames) + j
            
            if j < 3*Kdyn_frames:
                tj = 0.
            elif j > 3*Kdyn_frames+Mdyn_frames:
                tj = tmax
            else:
                tj = sin((j-3*Kdyn_frames)*dt*pi/2)*tmax
                
            si, tj = np.float64((ns[i], tj))
            
            Rij = fhomo( si, tj)
            R[:,:,ij] = A[:,:,j]@Rij
    
    return R

def vertical_translation_homotopy( steps = 6, step_frames = 30,
        rest_frames = 6, margin_frames = 12, grid_points = 241):
    
    total_frames = 2*margin_frames + steps*(step_frames+rest_frames) + rest_frames
    
    vert = np.zeros(( 3, grid_points, total_frames))
    
    t = np.linspace( 0, 1, step_frames)
    z = 10*t*(1-t)
    z_repeat = np.zeros(total_frames)
    
    for i in range(steps):
        
        start = margin_frames + rest_frames + i*(step_frames+rest_frames)
        end = start + step_frames
        
        z_repeat[start: end] = z
    
    for j in range(grid_points):
        vert[2,j,:] = z_repeat
    
    return vert

# Spherical plot
def ndarray_spherical_homotopy(reduced_pair, Npoints, steps,
                               nonlinear_s=None):
    
    from numpy.linalg import norm
    
    homotopy = symbolic_spherical_homotopy(reduced_pair)
    fhomotopy = sm.lambdify((s,t),homotopy,"numpy")
    
    curves = np.zeros((3,steps,Npoints))
    
    if nonlinear_s is None:
        nonlinear_s = homotopies_nonlinear_s[reduced_pair]
        
    if nonlinear_s:
        ns = (np.sin(np.linspace(-np.pi/2,np.pi/2,steps))+1)/2
    else:
        ns = np.linspace(0,1,steps)
        
    nt = np.linspace(0,1,Npoints)
        
    for i in range(steps):
        for j in range(Npoints):
            
            cij = fhomotopy(ns[i],nt[j])[:,0]
            
            curves[:,i,j] = cij/norm(cij)
    
    return curves