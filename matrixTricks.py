"""
Created on Wed Apr 21 13:16:59 2021

Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
"""

import sympy as sym

cos, sin, pi = sym.cos, sym.sin, sym.pi

# Time paramter t
t = sym.Symbol( 't' )

# Half-kickflip matrix
hk = sym.Matrix([[cos(pi*t), 0, -sin(pi*t)],
                 [0        , 1, 0        ],
                 [sin(pi*t), 0,cos(pi*t)]]);


# Half-heelflip matrix
hh = sym.Matrix([[cos(-pi*t), 0, -sin(-pi*t)],
                 [0         , 1, 0         ],  
                 [sin(-pi*t), 0, cos(-pi*t)]]);



# Frontside shove-it matrix
fs = sym.Matrix([[cos(pi*t), -sin(pi*t), 0],
                 [sin(pi*t), cos(pi*t) , 0],    
                 [0        , 0         , 1]]);



# Backside-shoveit matrix
bs = sym.Matrix([[cos(-pi*t), -sin(-pi*t), 0],
                 [sin(-pi*t), cos(-pi*t) , 0],    
                 [0         , 0          , 1]]);

# 180 degrees right-handed rotation around the x-axis
ui = sym.Matrix([[1, 0        , 0         ],
                 [0, cos(pi*t), -sin(pi*t)],    
                 [0, sin(pi*t), cos(pi*t) ]]);

# 180 degrees left-handed rotation around the x-axis
di = sym.Matrix([[1, 0         , 0          ],
                 [0, cos(-pi*t), -sin(-pi*t)],    
                 [0, sin(-pi*t), cos(-pi*t) ]]);

# Dictionary for the collection of tricks.
tricks = {'kickflip': hk*hk,

          'varialkickflip': fs*hk*hk,
    
          'hardflip': ui*hk,
          
          'shoveit' : bs,
          
          'shuvit' : bs,
          
          'popshoveit' : bs,
    
          'frontsideshoveit': fs,
          
          'frontsideshuvit': fs,
          
          'frontsidepopshoveit': fs,
    
          'heelflip' : hh*hh,
    
          'inwardheelflip' : bs*hh*hh,
    
          '360popshoveit' : bs*bs,
          
          '360shoveit' : bs*bs,
          
          '360shuvit' : bs*bs,
    
          'frontside360popshoveit' : fs*fs,
          
          'frontside360shoveit' : fs*fs,
          
          'frontside360shuvit' : fs*fs,
    
          'doublekickflip' : hk*hk*hk*hk,
    
          'triplekickflip' : hk*hk*hk*hk*hk*hk,
    
          'doubleheelflip' : hh*hh*hh*hh,
    
          'nightmareflip' : bs*hk*hk*hk*hk,
    
          'varialheelflip' : fs*hh*hh,
    
          '360flip' : bs*bs*hk*hk,
    
          'laserflip' : fs*fs*hh*hh,
    
          '360hardflip' : fs*fs*hk*hk } ;