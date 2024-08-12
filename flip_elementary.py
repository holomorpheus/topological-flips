"""
Elementary Fliptricks

Current version: Jul 25 2024
Created: Apr 21 2021

Author: Gabriel Martins (@holomorpheus)
Contributor: José Bravo (@jbravo87)
"""

# Libraries
import numpy as np
import sympy as sm

from sympy import cos, sin, pi, sqrt
from sympy import Quaternion as qn

# Local import
import name_functions as NF

# Time parameter t
t = sm.Symbol( 't' )

def elementary_flip_rotations():
    
    # Kickflip matrix
    kf = sm.Matrix([[ 1,       0     ,      0      ],
                    [ 0,  cos(2*pi*t), sin(2*pi*t) ],    
                    [ 0, -sin(2*pi*t), cos(2*pi*t) ]])
    
    
    # Heelflip matrix
    hf = sm.Matrix([[ 1,      0     ,       0      ],
                    [ 0, cos(2*pi*t), -sin(2*pi*t) ],    
                    [ 0, sin(2*pi*t),  cos(2*pi*t) ]])
    
    # Frontside shove-it matrix
    fs = sm.Matrix([[ cos(pi*t), -sin(pi*t), 0 ],
                    [ sin(pi*t),  cos(pi*t), 0 ],    
                    [     0    ,      0    , 1 ]])
    
    # Backside shove-it matrix
    bs = sm.Matrix([[  cos(pi*t), sin(pi*t), 0 ],
                    [ -sin(pi*t), cos(pi*t), 0 ],    
                    [      0    ,     0    , 1 ]])
    
    # 180 degrees left-handed rotation around the y-axis
    ui = sm.Matrix([[ cos(pi*t), 0, -sin(pi*t) ],
                    [     0    , 1,      0     ],
                    [ sin(pi*t), 0,  cos(pi*t) ]])
    
    # 180 degrees right-handed rotation around the y-axis
    di = sm.Matrix([[  cos(pi*t), 0, sin(pi*t) ],
                    [      0    , 1,     0     ],
                    [ -sin(pi*t), 0, cos(pi*t) ]])
    
    # Half-kickflip matrix
    hk = sm.Matrix([[ 1,      0    ,     0     ],
                    [ 0,  cos(pi*t), sin(pi*t) ],    
                    [ 0, -sin(pi*t), cos(pi*t) ]])
    
    return kf, hf, fs, bs, ui, di, hk

def elementary_flip_quaternions():
    
    # Kickflip quaternion
    kf = qn(cos(pi*t), -sin(pi*t), 0, 0)
    
    # Heelflip quaternion
    hf = qn(cos(pi*t), sin(pi*t), 0, 0)
    
    # Backside shove-it quaternion
    bs = qn(cos(pi*t/2), 0, 0, -sin(pi*t/2))
    
    # Frontside shove-it quaternion
    fs = qn(cos(pi*t/2), 0, 0, sin(pi*t/2))
    
    # Half-kickflip quaternion
    hk = qn(cos(pi*t/2), -sin(pi*t/2), 0, 0)
    
    # 180 degrees left-handed rotation around the y-axis
    ui = qn(cos(pi*t/2), 0, -sin(pi*t/2), 0)
    
    # 180 degrees right-handed rotation around the y-axis
    di = qn(cos(pi*t/2), 0, sin(pi*t/2), 0)
    
    return kf, hf, fs, bs, ui, di, hk