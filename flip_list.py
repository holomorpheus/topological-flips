"""
Flip List

Current version: Jul 25 2024
Created: Apr 21 2021

Author: Gabriel Martins (@holomorpheus)
Contributor: José Bravo (@jbravo87)
"""

# Libraries
import numpy as np
import sympy as sm

from sympy import cos, sin, pi, sqrt

# Local module
import name_functions as NF
from flip_elementary import t
from flip_elementary import elementary_flip_rotations
from flip_elementary import elementary_flip_quaternions

# Functions
def generate_flip_dictionary(quaternion=False):
    
    if quaternion:
        
        kf, hf, fs, bs, ui, di, hk = elementary_flip_quaternions()
        
    else:
        
        kf, hf, fs, bs, ui, di, hk = elementary_flip_rotations()
    
    def ollie():
        if quaternion:
            return sm.Quaternion(1,0,0,0)
        else:
            return sm.eye(3)
    
    def shoveit():
        return bs
    
    def fsshoveit():
        return fs
    
    def kickflip():
        return kf
    
    def heelflip():
        return hf
    
    def varialflip():
        F= bs*kf
        F.simplify()
        return F
    
    def hardflip():
        F = fs*kf
        F.simplify()
        return F
    
    def inwardheelflip():
        F = bs*hf
        F.simplify()
        return F
    
    def varialheelflip():
        F = fs*hf
        F.simplify()
        return F
        
    def muskahardflip():
        F = ui*hk
        F.simplify()
        return F
    
    def dolphinflip():
        F = di*hk
        F.simplify()
        return F
    
    def three60shoveit():
        F = bs*bs
        F.simplify()
        return F
    
    def fs360shoveit():
        F = fs*fs
        F.simplify()
        return F
    
    def five40shoveit():
        F = bs*bs*bs
        F.simplify()
        return F
    
    def fs540shoveit():
        F = fs*fs*fs
        F.simplify()
        return F
    
    def doublekickflip():
        F = kf*kf
        F.simplify()
        return F
    
    def triplekickflip():
        F = kf*kf*kf
        F.simplify()
        return F
    
    def doubleheelflip():
        F = hf*hf
        F.simplify()
        return F
    
    def varialdoubleflip():
        F = bs*kf*kf
        F.simplify()
        return F
    
    def three60flip():
        F = bs*bs*kf
        F.simplify()
        return F
    
    def laserflip():
        F = fs*fs*hf
        F.simplify()
        return F
    
    def three60hardflip():
        F = fs*fs*kf
        F.simplify()
        return F
    
    def reversevarialflip():
        F = kf*bs
        F.simplify()
        return F
    
    def wobbling360shoveit():
        
        omega = 3
        A = 1/3
        
        a = cos(pi*t)
        b = -sin(pi*t)*A*sin(2*pi*omega*t)
        c = 0
        d = -sin(pi*t)*sqrt(1-A**2)
        
        q = sm.Quaternion(a,b,c,d)
        q.simplify()
        
        if quaternion:
            return q
        else:
            return q.to_rotation_matrix()

    flip_dict = { 'ollie' : ollie,
                  'shoveit' : shoveit,
                  'fsshoveit': fsshoveit,
                  'kickflip' : kickflip,
                  'heelflip' : heelflip,
                  'varialflip': varialflip,
                  'hardflip' : hardflip,
                  'muskahardflip': muskahardflip,
                  'dolphinflip': dolphinflip,
                  'inwardheelflip' : inwardheelflip, 
                  'varialheelflip' : varialheelflip,
                  '360shoveit' : three60shoveit,
                  'fs360shoveit' : fs360shoveit,
                  '540shoveit' : five40shoveit,
                  'fs540shoveit' : fs540shoveit,
                  'doublekickflip' : doublekickflip,
                  'triplekickflip' : triplekickflip,
                  'doubleheelflip' : doubleheelflip,
                  'varialdoubleflip' : varialdoubleflip,
                  'nightmareflip' : varialdoubleflip,
                  '360flip' : three60flip,
                  'laserflip' : laserflip,    
                  '360hardflip' : three60hardflip,
                  'reversevarialflip' : reversevarialflip,
                  'wobbling360shoveit' : wobbling360shoveit}
    
    return flip_dict

def symbolic_rotation_flip(name):
    
    name = NF.reduce_name(name)
    flip_dictionary = generate_flip_dictionary()
    
    return flip_dictionary[name]()

def symbolic_quaternion_flip(name):
    
    name = NF.reduce_name(name)
    flip_dictionary = generate_flip_dictionary(quaternion=True)
    
    return flip_dictionary[name]()
