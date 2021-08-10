"""
Created on Aug 10 2021

Author:
    Gabriel Martins
    José Bravo
"""

# Imports
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import misc

import os
from mpl_toolkits.mplot3d import Axes3D
from subprocess import call

def frame_number(i, total_frames):
    
    if i < 10:
        if total_frames < 100:
            s = "0" + str(i)
        elif total_frames < 1000:
            s = "00" + str(i)
        else:
            raise ValueError("The number of frames exceeds 999.")
    elif i < 100:
        if total_frames > 99:
            s = "0" + str(i)
        else:
            s = str(i)
    else:
        s = str(i)
    
    return s
    
def skate_curve(width, length):
        
    cos = np.cos;
    sin = np.sin;
    pi = np.pi;

    dx, dy = width, length;

    gridpts = 20;
    t = np.linspace(0, 1, gridpts);

    x = np.empty(2*gridpts+1);
    y = np.empty(2*gridpts+1);
    z = np.empty(2*gridpts+1);

    x[:gridpts] = cos(pi*t);
    y[:gridpts] = sin(pi*t) + dy;
    z[:gridpts] = .3*(-cos(2*pi*t)+1);

    x[gridpts:2*gridpts] = cos(pi*(1-t));
    y[gridpts:2*gridpts] = -sin(pi*(1-t)) - dy;
    z[gridpts:2*gridpts] = .3*(-cos(2*pi*t)+1);

    x[-1], y[-1], z[-1] = np.array([dx, dy, 0]);
    
    return np.array([x, y, z])

def generate_frames(symb_R, title, dyn_frames=60, static_frames=18, vertical = True):

    if not os.path.exists("animation"):
        os.mkdir("animation")

    # Relevant mathematical functions and constants
    cos = np.cos
    sin = np.sin
    pi = np.pi

    dx, dy = 1, 3.5;

    P0 = skate_curve(dx, dy);

    ax = plt.axes(projection='3d');

    # Create the frames
    # Create initial static frames
    ax.set_xticks([-dy, -dy/2, 0, dy/2, dy])
    ax.set_yticks([-dy, -dy/2, 0, dy/2, dy])
    ax.set_zticks([-dy, -dy/2, 0, dy/2, dy])

    ax.axes.set_xlim3d(left=-dy-1, right=dy+1)
    ax.axes.set_ylim3d(bottom=-dy-1, top=dy+1)
    ax.axes.set_zlim3d(bottom=-dy-1, top=dy+1)

    ax.set_title(title)

    x0 = P0[0, :];
    y0 = P0[1, :];
    z0 = P0[2, :];
    
    ax.plot(x0, y0, z0)
    
    for i in range(int(static_frames/2)):
        
            si = frame_number(i, dyn_frames+static_frames);
            plt.savefig("animation/" + si + ".png", bbox_inches='tight')
            
            j = int(i + dyn_frames + static_frames/2);
            sf = frame_number(j, dyn_frames+static_frames);
            plt.savefig("animation/" + sf + ".png", bbox_inches='tight')

    ax.clear()
    
    for i in range(dyn_frames):
        
        ax.set_xticks([-dy, -dy/2, 0, dy/2, dy])
        ax.set_yticks([-dy, -dy/2, 0, dy/2, dy])
        ax.set_zticks([-dy, -dy/2, 0, dy/2, dy])

        ax.axes.set_xlim3d(left=-dy-1, right=dy+1)
        ax.axes.set_ylim3d(bottom=-dy-1, top=dy+1)
        ax.axes.set_zlim3d(bottom=-dy-1, top=dy+1)

        ax.set_title(title)
        
        t = sym.Symbol( 't' );
        
        ti = i/(dyn_frames - 1);

        Ri = symb_R.subs(t, ti);
        Ri = np.array(Ri).astype(np.float64);
        P = Ri@P0;

        xi = P[0, :];
        yi = P[1, :];
        zi = P[2, :];
        
        if vertical:
            dh = (dy+2)*sin(pi*ti);
            zi = zi + dh;

        ax.plot(xi, yi, zi)
        
        j = int(i + static_frames);
        
        s = frame_number(j, dyn_frames+static_frames);
            
        plt.savefig("animation/" + s + ".png", bbox_inches='tight')
        ax.clear()

def animate(symb_R, title, filename,
                     os, file_type,
                     dyn_frames=60, static_frames=18,
                     delete_frames=True):
    
    os = Misc.clean_name(os);
    
    file_type = Misc.clean_name(file_type);
    file_type = "."+file_type;

    if os != "windows" and os != "macos":
        raise NameError("The operating system is not valid")
        
    if file_type != ".gif" and file_type != ".mp4":
        raise NameError("The file type is not valid")

    if os == "windows":

        generate_frames(symb_R, title, dyn_frames, static_frames)
        
        # Create animation. Requires ImageMagick
        
        cmd1 = 'cd animation';
        cmd2 = 'convert *.png ' + filename + file_type;

        total_cmd = cmd1 + '&&' + cmd2
        call(total_cmd, shell=True)

        if delete_frames == True:
            # Clean up frame png files
            cmd1 = 'cd animation';
            cmd2 = 'del /s /q *.png';
            
            total_cmd = cmd1 + '&&' + cmd2;
            call(total_cmd, shell=True)

    if os == "macos":

        generate_frames(symb_R, title, dyn_frames = dyn_frames, static_frames = static_frames)

        # Create animation. Requires ImageMagick
        
        # If delay = N then FPS = 100/N
        
        call("cd animation && convert -delay 4 *.png " + filename + file_type, shell=True)

        if delete_frames == True:
            # Clean up frame png files
            call("rm -f animation/*.png", shell=True)