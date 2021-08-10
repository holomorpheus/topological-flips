"""

Created on Wed Jan 15 2021

A class for skateboard tricks

Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
    
"""

import matrixTricks
import skateAnimation
import misc

class SkateTrick:

    def __init__(self, name):

        '''
        Initialization method

        Parameters
        ----------
        name : str
            Name of the skateboard trick.
        '''

        self.name = misc.clean_name(name);
        self.matrix = matrixTricks.tricks[self.name];
        self.matrix.simplify()
        self.title = matrixTricks.plot_titles[self.name];

    # A dictionary for the plot titles of different tricks

    def changetrick(self, name):
        '''
            Change name and matrix to a new trick.
        '''

        self.name = misc.clean_name(name)
        self.matrix = matrixTricks.tricks[self.name]
        self.matrix.simplify()
        self.title = matrixTricks.plot_titles[self.name];

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


    def animate(self, op_syst, file_type, dyn_frames=60, static_frames=18, delete_frames=True):
        
        skateAnimation.animate(self.matrix, self.title, self.name,
                               op_syst, file_type,
                               dyn_frames, static_frames)
            


         
        