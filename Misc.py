"""
Created on Aug 10 2021

Author:
    Gabriel Martins
    José Bravo
"""

def clean_name(name):

        '''
        
        Name cleaning function.

        Takes a string and removes unnecessary characters, spaces,
        or capitalization.
        
        Parameters
        ----------
        name : str

        Returns
        -------
        newname : str
            The processed name.

        '''

        newname = ""
        
        for i in range(len(name)):
            
            char = name[i];
            
            if ord(char) > 96 and ord(char) < 123:
                newname += char;
                
            elif ord(char) > 64 and ord(char) < 91:
                newname += chr(ord(char)+32);
            
            elif ord(char) > 47 and ord(char) < 58:
                newname += char;
                
        return newname
    
    