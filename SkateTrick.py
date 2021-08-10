"""

Created on Wed Jan 15 2021

A class for skateboard tricks

Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
    
"""

import matrixTricks
import skateAnimation
import Misc

class SkateTrick:

    def __init__(self, name):

        '''
        Initialization method

        Parameters
        ----------
        name : str
            Name of the skateboard trick.
        '''

        self.name = Misc.clean_name(name);
        self.matrix = matrixTricks.tricks[self.name];
        self.matrix.simplify()
        self.title = self.plot_titles[self.name];

    # A dictionary for the plot titles of different tricks
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
        '''
            Change name and matrix to a new trick.
        '''

        self.name = Misc.clean_name(name)
        self.matrix = matrixTricks.tricks[self.name]
        self.matrix.simplify()
        self.title = self.plot_titles[self.name]

    def tricknames(self):
        '''Prints the list of tricks int the collection.'''
        for i in matrixTricks.tricks.keys():
            print(i)
        
    def generate_frames(self, dyn_frames=60, static_frames=18):
        '''
        Creates frames for the trick's animation.

        Parameters
        ----------
        dyn_frames : int
            Number of frames during the trick's movement.
        static_frames : int
            Number of frames at rest.
        '''
        
        skateAnimation.generate_frames(self.matrix, self.title, dyn_frames, static_frames)


    def animate(self, os, file_type, dyn_frames=60, static_frames=18, delete_frames=True):
        
        skateAnimation.animate(self.matrix, self.title, self.name,
                     os, file_type,
                     dyn_frames, static_frames)
            


         
        