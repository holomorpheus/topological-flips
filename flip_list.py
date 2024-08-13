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
    
    def three60shoveit():
        F = bs*bs
        F.simplify()
        return F
    
    def fs360shoveit():
        F = fs*fs
        F.simplify()
        return F
    
    def kickflip():
        return kf
    
    def heelflip():
        return hf
    
    def five40shoveit():
        F = bs*bs*bs
        F.simplify()
        return F
    
    def fs540shoveit():
        F = fs*fs*fs
        F.simplify()
        return F
    
    def varialflip():
        F= bs*kf
        F.simplify()
        return F
    
    def hardflip():
        F = fs*kf
        F.simplify()
        return F
    
    def varialheelflip():
        F = fs*hf
        F.simplify()
        return F
    
    def inwardheelflip():
        F = bs*hf
        F.simplify()
        return F
    
    def seven20shoveit():
        F = bs*bs*bs*bs
        F.simplify()
        return F
    
    def fs720shoveit():
        F = fs*fs*fs*fs
        F.simplify()
        return F
    
    def doublekickflip():
        F = kf*kf
        F.simplify()
        return F
    
    def doubleheelflip():
        F = hf*hf
        F.simplify()
        return F
    
    def three60flip():
        F = bs*bs*kf
        F.simplify()
        return F
    
    def three60hardflip():
        F = fs*fs*kf
        F.simplify()
        return F
    
    def laserflip():
        F = fs*fs*hf
        F.simplify()
        return F
    
    def three60inwardheelflip():
        F = bs*bs*hf
        F.simplify()
        return F
    
    def varialdoubleflip():
        F = bs*kf*kf
        F.simplify()
        return F
    
    def five40flip():
        F = bs*bs*bs*kf
        F.simplify()
        return F
    
    def triplekickflip():
        F = kf*kf*kf
        F.simplify()
        return F
    
    def tripleheelflip():
        F = hf*hf*hf
        F.simplify()
        return F
    
    def quadflip():
        F = kf*kf*kf*kf
        F.simplify()
        return F
    
    def quadheelflip():
        F = hf*hf*hf*hf
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
    
    def wobblingkickflip():
        
        omega = 3
        A = 1/3
        
        a = cos(pi*t)
        b = -sin(pi*t)*sqrt(1-A**2)
        c = 0
        d = -sin(pi*t)*A*sin(2*pi*omega*t)
        
        q = sm.Quaternion(a,b,c,d)
        q.simplify()
        
        if quaternion:
            return q
        else:
            return q.to_rotation_matrix()

    flip_dict = { 'ollie' : ollie,
                  'shoveit' : shoveit,
                  'fsshoveit': fsshoveit,
                  '360shoveit' : three60shoveit,
                  'fs360shoveit' : fs360shoveit,
                  'kickflip' : kickflip,
                  'heelflip' : heelflip,
                  '540shoveit' : five40shoveit,
                  'fs540shoveit' : fs540shoveit,
                  'varialflip': varialflip,
                  'hardflip' : hardflip,
                  'varialheelflip' : varialheelflip,
                  'inwardheelflip' : inwardheelflip,
                  '720shoveit' : seven20shoveit,
                  'fs720shoveit' : fs720shoveit,
                  'doublekickflip' : doublekickflip,
                  'doubleheelflip' : doubleheelflip,
                  '360flip' : three60flip,
                  '360hardflip' : three60hardflip,
                  'laserflip' : laserflip,
                  '360inwardheelflip' : three60inwardheelflip,
                  'varialdoubleflip' : varialdoubleflip,
                  '540flip' : five40flip,
                  'triplekickflip' : triplekickflip,
                  'tripleheelflip' : tripleheelflip,
                  'quadflip' : quadflip,
                  'quadheelflip' : quadheelflip,
                  'muskahardflip': muskahardflip,
                  'dolphinflip': dolphinflip,
                  'reversevarialflip' : reversevarialflip,
                  'wobbling360shoveit' : wobbling360shoveit,
                  'wobblingkickflip' : wobblingkickflip}
    
    return flip_dict

def symbolic_rotation_flip(name):
    
    name = NF.reduce_name(name)
    flip_dictionary = generate_flip_dictionary()
    
    return flip_dictionary[name]()

def symbolic_quaternion_flip(name):
    
    name = NF.reduce_name(name)
    flip_dictionary = generate_flip_dictionary(quaternion=True)
    
    return flip_dictionary[name]()
