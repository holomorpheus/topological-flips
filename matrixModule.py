"""
Created on Wed Apr 21 13:16:59 2021

Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
"""

import sympy as sym

# Learn how to hide certain attributes

cos, sin, pi = sym.cos, sym.sin, sym.pi

 

# First, will establish the temporal parameter as t

t = sym.Symbol( 't' )


# Will use hk as the variable name for the half-kickflip matrix

hk = sym.Matrix([[cos(pi*t), 0, -sin(pi*t)],

                 [0        , 1, 0        ],
    
                 [sin(pi*t), 0,cos(pi*t)]]);



# Will use hh as the variable name for the half-heelflip matrix

hh = sym.Matrix([[cos(-pi*t), 0, -sin(-pi*t)],

                 [0         , 1, 0         ],
    
                 [sin(-pi*t), 0, cos(-pi*t)]]);



# Now to define the frontside-shoveit matrix

# Will use fs as the variable for the matrix

fs = sym.Matrix([[cos(pi*t), -sin(pi*t), 0],

                 [sin(pi*t), cos(pi*t) , 0],
    
                 [0        , 0         , 1]]);



# Now to define the backside-shoveit matrix

# Will use bs as the variable for the matrix

bs = sym.Matrix([[cos(-pi*t), -sin(-pi*t), 0],

                 [sin(-pi*t), cos(-pi*t) , 0],
    
                 [0         , 0          , 1]]);



# Define ui to be the variable for the matrix of

# 180 degrees rotation around the intermediate axis

# with the front of the skateboard going upward

ui = sym.Matrix([[1, 0        , 0         ],

                 [0, cos(pi*t), -sin(pi*t)],
    
                 [0, sin(pi*t), cos(pi*t) ]]);





# Define di to be the variable for the matrix of

# 180 degrees rotation around the intermediate axis

# with the front of the skateboard going upward

di = sym.Matrix([[1, 0         , 0          ],

                 [0, cos(-pi*t), -sin(-pi*t)],
    
                 [0, sin(-pi*t), cos(-pi*t) ]]);



# Dictionary for our collection of tricks.

# Remove spaces from dictionary indices

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