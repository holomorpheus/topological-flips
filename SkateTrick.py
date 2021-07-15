"""
Created on Wed Jan 15 2021

A class for skateboard tricks

Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
"""

import sympy as sym
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matrixModule

def clean_name(name):

        '''Name cleaning function.

        Will take user input and remove any unnecessary characters, spaces,
        or capitalization. Will then match the return to dictionary of tricks.

        Returns
        -------
        newname : str
            The processed name of the skateboard trick.

        '''

        newname = ""
        for i in range(len(name)):
            char = name[i]
            if ord(char) > 96 and ord(char) < 123:
                newname += char
            if ord(char) > 64 and ord(char) < 91:
                newname += chr(ord(char)+32)
        return newname

class SkateTrick:

    def __init__(self, name):

        '''The initialization method

        Parameters
        ----------
        self.name : str
            User input for the skateboard trick of interest.
        self.matrix : str
            Cross-reference 'name' with matrixModule to find rotational matrix.
            It is a symbolic matrix using SymPy.
        self.title : str
            Parameter will also be used to find the plot title for the GIFs.

        Variables
        ---------
        os : str
            Defaults to Windows operating system. Can also choose OSX.

        '''

        self.name = clean_name(name)
        self.matrix = matrixModule.tricks[self.name]
        self.matrix.simplify()
        self.title = self.plot_titles[self.name]

    # Create a dictionary for all the titles for different tricks
    # Words start with upper case letters and are spaced
    plot_titles = {'kickflip': 'Kickflip',
                   'varialkickflip': 'Varial Kickflip',
                   'hardflip': 'Hardflip',
                   'frontsideshoveit': 'Frontside Shove-it',
                   'frontsidepopshoveit': 'Frontside Pop Shove-it',
                   'frontsideshuvit': 'Frontside Shuvit',
                   'heelflip': 'Heelflip',
                   'inwardheelflip': 'Inward Heelflip',
                   '360popshoveit': '360 Pop Shove-it',
                   '360shoveit': '360 Shove-it',
                   '360shuvit': '360 Shuvit',
                   'frontside360popshoveit': 'Frontside 360 Pop Shove-it',
                   'frontside360shoveit': 'Frontside 360 Shove-it',
                   'frontside360shuvit': 'Frontside 360 Shuvit',
                   'doublekickflip': 'Double Kickflip',
                   'triplekickflip': 'Triple Kickflip',
                   'doubleheelflip': 'Double Heelflip',
                   'nightmareflip': 'Nightmare Flip',
                   'varialheelflip': 'Varial Heelflip',
                   '360flip': '360 Flip',
                   'laserflip': 'Laser Flip',
                   '360hardflip': '360 Hardflip'}

    def changetrick(self, name):
        '''Change name and matrix to a new trick.

        Will follow similar logic to the initial method.
        That is, will assign a new matrix and plot title.

        '''

        self.name = clean_name(name)
        self.matrix = matrixModule.tricks[self.name]
        self.matrix.simplify()
        self.title = self.plot_titles[self.name]

    def tricknames(self):
        '''Method to print the list of possible tricks from the dictionary.'''
        for i in matrixModule.tricks.keys():
            print(i)

    def create_frames(self, dyn_frames, static_frames):
        '''Largest method in script used to create frames

        Will create a directory/folder called frames if it doesn't exist.
        Method creates dynamic and static frames. Will use symbolic matrices
        from matrixModule to create frames of the trick. Also defaulted
        to clear frames after use.

        Parameters
        ----------
        dx, dy : int, float
            Creates the skateboard curve.
        P0 : float
            NumPy array to store the Cartesian coord. of the skateboard.
        trick : str
            Stores (creates) symbolic matrix for the trick.
        fig : figure
            Creates the figure that is the skateboard.
        ax : axes
            The 3D axes to visualize the skateboard
        title : str
            The title of the plot corresponding to a trick.
        t : float
            Produces the frames in successive order.
        sym_R : SymPy Matrix
            Will redefine t in symoblic matrix from original definition.
        R : float
            Converts the symbolic matrix into a numeric one.
        P : float
            Uses the matrix multiplication operator to update trick.

        '''

        if not os.path.exists("flipgifs"):
            os.mkdir("flipgifs")

        # Relevant mathematical functions and constants
        cos = np.cos
        sin = np.sin
        pi = np.pi

        dx, dy = 1, 3.5

        gridpts = 20
        t = np.linspace(0, 1, gridpts)

        x = np.empty(2*gridpts+1)
        y = np.empty(2*gridpts+1)
        z = np.empty(2*gridpts+1)

        x[:gridpts] = cos(pi*t)
        y[:gridpts] = sin(pi*t) + dy
        z[:gridpts] = .3*(-cos(2*pi*t)+1)

        x[gridpts:2*gridpts] = cos(pi*(1-t))
        y[gridpts:2*gridpts] = -sin(pi*(1-t)) - dy
        z[gridpts:2*gridpts] = .3*(-cos(2*pi*t)+1)

        x[-1], y[-1], z[-1] = np.array([dx, dy, 0])

        P0 = np.array([x, y, z])

        trick = self.matrix

        fig = plt.figure(figsize=(8, 10))
        ax = plt.axes(projection='3d')
        title = self.title

        # Create the frames
        # Create initial static frames
        ax.set_xticks([-dy, -dy/2, 0, dy/2, dy])
        ax.set_yticks([-dy, -dy/2, 0, dy/2, dy])
        ax.set_zticks([-dy, -dy/2, 0, dy/2, dy])

        ax.axes.set_xlim3d(left=-dy-1, right=dy+1)
        ax.axes.set_ylim3d(bottom=-dy-1, top=dy+1)
        ax.axes.set_zlim3d(bottom=-dy-1, top=dy+1)

        plt.title(title)

        ax.plot(x, y, z)

        for i in range(int(static_frames/2)):
            if i < 10:
                s = "0" + str(i)
            else:
                s = str(i)
            plt.savefig("flipgifs/" + s + ".png", bbox_inches='tight')
            k = int(i + dyn_frames + static_frames/2)
            plt.savefig("flipgifs/" + str(k) + ".png", bbox_inches='tight')

        ax.clear()

        for i in range(dyn_frames):

            ax.set_xticks([-dy, -dy/2, 0, dy/2, dy])
            ax.set_yticks([-dy, -dy/2, 0, dy/2, dy])
            ax.set_zticks([-dy, -dy/2, 0, dy/2, dy])

            ax.axes.set_xlim3d(left=-dy-1, right=dy+1)
            ax.axes.set_ylim3d(bottom=-dy-1, top=dy+1)
            ax.axes.set_zlim3d(bottom=-dy-1, top=dy+1)

            plt.title(title)

            t = i/(dyn_frames - 1)

            sym_R = (trick).subs(matrixModule.t, t)
            R = np.array(sym_R).astype(np.float64)
            P = R@P0

            dh = (dy+2)*sin(pi*i/(dyn_frames-1))

            xi = P[0, :]
            yi = P[1, :]
            zi = P[2, :] + dh

            ax.plot(xi, yi, zi)
            j = int(i + static_frames/2)
            if j < 10:
                s = "0" + str(j)
            else:
                s = str(j)
            plt.savefig("flipgifs/" + s + ".png", bbox_inches='tight')
            ax.clear()

    def create_animation(self, os, file_type, dyn_frames=60, static_frames=10, delete_frames=True):

        if os != "windows" and os != "osx":
            raise NameError("The operating system is not valid")
            
        if file_type != ".gif" and file_type != ".mp4":
            raise NameError("The file type is not valid")

        if os == "windows":
            filename = self.name

            self.create_frames(dyn_frames, static_frames)
            from subprocess import call
            cmd1 = 'cd flipgifs'
            cmd2 = 'convert *.png ' + filename + file_type

            total_cmd = cmd1 + '&&' + cmd2
            call(total_cmd, shell=True)

            if delete_frames == True:
                # if delete_frames:
                # Optional: clean up frame png files
                call("rm -f flipgifs/*.png", shell=True)

        if os == "osx":
            filename = self.name

            self.create_frames(dyn_frames, static_frames)

            # Convert to gif (works on linux/os-x, requires image-magick)
            from subprocess import call
            call("cd flipgifs && convert -delay 3 *.png " + filename + file_type, shell=True)

            if delete_frames == True:
                # Optional: clean up frame png files
                call("rm -f flipgifs/*.png", shell=True)


         
        