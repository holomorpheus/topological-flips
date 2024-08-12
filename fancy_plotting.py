"""
Fancy Plotting Functions

Current version: Jul 25 2024
Created: Apr 21 2021

Author: Gabriel Martins (@holomorpheus)
"""

import numpy as np
from numpy import pi, cos, sin

def fast_to_slow(t0, t1, grid_points):
    
    
    s = np.linspace( 0, pi/2, grid_points)
    
    s = (t1-t0)*sin(s)+t0
    
    return s

def pop_rotation(Nframes = 60):
        
    def Ry(t):    
        
        A = np.array([[ cos(t), 0, -sin(t) ],
                      [    0  , 1,    0    ],
                      [ sin(t), 0,  cos(t) ]])
        
        return A
        
    Kframes = int(Nframes/16)
    Mframes = Nframes - 4*Kframes
    
    s1 = fast_to_slow(0, pi/6, 3*Kframes+1) 
    s2 = fast_to_slow(pi/6, 0, Mframes)
    s3 = np.zeros(Kframes+1)
    s = np.concatenate((s1[:-1],s2))
    s = np.concatenate((s[:-1],s3))
        
    Ay = np.zeros((3,3,Nframes))
    
    for i in range(Nframes):
        
        Ay[:,:,i] = Ry(s[i])
        
    return Ay
