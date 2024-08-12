"""
Homotopy List

Current version Aug 11 2024
Created Jul 25 2024

Author: Gabriel Martins (@holomorpheus)
"""

# Libraries
import sympy as sm
from sympy import cos, sin, pi, sqrt
from sympy import Quaternion as qn

# Local import
import flip_list as FL

# Homotopy parameters s and t
s = sm.symbols('s')
t = sm.Symbol( 't' )

# List of homotopies

def kickflip_to_heelflip():
    
    a = cos(pi*t)
    b = -sin(pi*t)*cos(pi*s)
    c = 0
    d = -sin(pi*t)*sin(pi*s)
    
    return qn(a,b,c,d)
    
def heelflip_to_kickflip():
    
    q = kickflip_to_heelflip()
    q = q.subs(s,1-s)
    
    return q

def three60shoveit_to_fs360shoveit():
    
    a = cos(pi*t)
    b = sin(pi*t)*sin(pi*s)
    c = 0
    d = -sin(pi*t)*cos(pi*s)

    return qn(a,b,c,d)

def fs360shoveit_to_360shoveit(spherical=False):
    
    q = three60shoveit_to_fs360shoveit()
    q = q.subs(s,1-s)
    
    return q

def kickflip_to_360shoveit():
        
    a = cos(pi*t)
    b = -cos(pi*s/2)*sin(pi*t)
    c = 0
    d = -sin(pi*s/2)*sin(pi*t)
    
    return qn(a,b,c,d)

def three60shoveit_to_kickflip():
    
    q = kickflip_to_360shoveit()
    q = q.subs(s,1-s)
    
    return q

def heelflip_to_360shoveit():
    
    a = cos(pi*t)
    b = cos(pi*s/2)*sin(pi*t)
    c = 0
    d = -sin(pi*s/2)*sin(pi*t)

    return qn(a,b,c,d)

def three60shoveit_to_heelflip():
    
    q = heelflip_to_360shoveit()
    q = q.subs(s,1-s)
    
    return q

def varialflip_to_540shoveit():
    
    # kickflip to 360 shove it quaternion components
    a = cos(pi*t)
    b = -cos(pi*s/2)*sin(pi*t)
    c = 0
    d = -sin(pi*s/2)*sin(pi*t)
    kickto360 = qn(a,b,c,d)
    shove = qn( cos(pi*t/2), 0, 0, -sin(pi*t/2))
    
    return shove*kickto360
    
def five40shoveit_to_varialflip():
    
    q = varialflip_to_540shoveit()
    q = q.subs(s,1-s)
    
    return q

def ollie_to_doublekickflip():
        
    a = s*cos(2*pi*t) + (1-s)
    b = -s*sin(2*pi*t)
    c = 0
    d = -sqrt(2*s*(1-s)*(1-cos(2*pi*t)))

    return qn(a,b,c,d)

def doublekickflip_to_ollie():
    
    q = ollie_to_doublekickflip()
    q = q.subs(s,1-s)
    
    return q

def varialflip_to_inwardheelflip():
    
    # Shove it
    a = cos(pi*t/2)
    b = 0
    c = 0
    d = -sin(pi*t/2)
    shove = qn(a,b,c,d)
    
    # Kickflip to heelflip
    a = cos(pi*t)
    b = -sin(pi*t)*cos(pi*s)
    c = 0
    d = -sin(pi*t)*sin(pi*s)
    kickflip_to_heelflip = qn(a,b,c,d)
    
    return shove*kickflip_to_heelflip
    
def inwardheelflip_to_varialflip():
    
    q = varialflip_to_inwardheelflip()
    q = q.subs(s,1-s)
    
    return q
    
def hardflip_to_varialheelflip():
    
    # Fs shove it
    a = cos(pi*t/2)
    b = 0
    c = 0
    d = sin(pi*t/2)
    fsshove = qn(a,b,c,d)
    
    # Kickflip to heelflip
    a = cos(pi*t)
    b = -sin(pi*t)*cos(pi*s)
    c = 0
    d = -sin(pi*t)*sin(pi*s)
    kickflip_to_heelflip = qn(a,b,c,d)
    
    return fsshove*kickflip_to_heelflip

def varialheelflip_to_hardflip():
    
    q = hardflip_to_varialheelflip()
    q = q.subs(s,1-s)
    
    return q

def shoveit_to_varialdoubleflip():
    
    # double kickflip to ollie
    a = s*cos(2*pi*t) + (1-s)
    b = -s*sin(2*pi*t)
    c = 0
    d = -sqrt(2*s*(1-s)*(1-cos(2*pi*t)))
    dkick_to_ollie = qn(a,b,c,d)
    
    shove = qn(cos(pi*t/2), 0, 0, -sin(pi*t/2))
    return shove*dkick_to_ollie

def varialdoubleflip_to_shoveit():
    
    q = shoveit_to_varialdoubleflip()
    q = q.subs(s,1-s)
    
    return q

def hardflip_to_muskahardflip():
        
    qhard = FL.symbolic_quaternion_flip('hardflip')
    qmuska = FL.symbolic_quaternion_flip('muskahardflip')
    
    homo = (1-s)*qhard + s*qmuska
    homo_norm = homo.norm()
    
    return homo/homo_norm
        
def muskahardflip_to_hardflip():
    
    q = hardflip_to_muskahardflip()
    q = q.subs(s,1-s)
    
    return q
    
# Deformation of a wobbly kickflip
def unwobbling_360shoveit():
    
    a = cos(pi*t)
    b = -sin(pi*t)*sin((pi/6)*s*sin(4*pi*t))
    c = 0
    d = -sin(pi*t)*cos((pi/6)*s*sin(4*pi*t))
    
    return qn(a,b,c,d)
    
# Deformation of a wobbly kickflip
def unwobbling_kick(spherical=False):
    
    a = cos(pi*t)
    b = -sin(pi*t)*cos((pi/10)*s*sin(4*pi*t))
    c = 0
    d = -sin(pi*t)*sin((pi/10)*s*sin(4*pi*t))
    
    return qn(a,b,c,d)

# Dictionary of deformations

quaternion_homotopies = {
    ('kickflip','heelflip'): kickflip_to_heelflip,
    ('heelflip','kickflip'): heelflip_to_kickflip,
    ('360shoveit','fs360shoveit'): three60shoveit_to_fs360shoveit,
    ('fs360shoveit','360shoveit'): fs360shoveit_to_360shoveit,
    ('kickflip','360shoveit'): kickflip_to_360shoveit,
    ('360shoveit','kickflip'): three60shoveit_to_kickflip,
    ('heelflip','360shoveit'): heelflip_to_360shoveit,
    ('360shoveit','heelflip'): three60shoveit_to_heelflip,
    ('varialflip','540shoveit'): varialflip_to_540shoveit,
    ('540shoveit','varialflip'): five40shoveit_to_varialflip,
    ('varialflip','inwardheelflip'): varialflip_to_inwardheelflip,
    ('inwardheelflip','varialflip'): inwardheelflip_to_varialflip,
    ('hardflip','varialheelflip'): hardflip_to_varialheelflip,
    ('varialheelflip','hardflip'): varialheelflip_to_hardflip,
    ('ollie','doublekickflip'): ollie_to_doublekickflip,
    ('doublekickflip','ollie'): doublekickflip_to_ollie,
    ('shoveit','varialdoubleflip'): shoveit_to_varialdoubleflip,
    ('varialdoubleflip','shoveit'): varialdoubleflip_to_shoveit,
    ('wobbling360shoveit','360shoveit') : unwobbling_360shoveit,
    ('wobblingkickflip','kickflip') : unwobbling_kick,
    ('hardflip','muskahardflip') : hardflip_to_muskahardflip,
    ('muskahardflip','hardflip') : muskahardflip_to_hardflip}

def symbolic_quaternion_homotopy(reduced_pair):
    
    return quaternion_homotopies[reduced_pair]()

def symbolic_spherical_homotopy(reduced_pair):
    
    q = quaternion_homotopies[reduced_pair]()
    a, b, c, d = q.to_Matrix()
    
    return sm.Matrix([a,-b,-d])

def symbolic_rotation_homotopy(reduced_pair):
    
    q = quaternion_homotopies[reduced_pair]()
    
    return q.to_rotation_matrix()


