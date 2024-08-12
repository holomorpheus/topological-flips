"""
Name Functions

Current version: July 23rd 2024
Created: Aug 10 2021

Author:
    Gabriel Martins
Contributor:
    José Bravo
"""

# Import
from collections import OrderedDict

def list_fliptricks():
    
    print("Flip tricks currently available:")
    
    fliplist = dict_trick_handle.values()
    
    fliplist = list(OrderedDict.fromkeys(fliplist))
    
    for flip in fliplist:
        
        print(dict_trick_titles[flip])
        
def list_homotopies():
    
    print("Flip homotopies currently available:")
    
    for homo in dict_def_titles.values():
        print(homo)
    
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
        
        for char in name:
            
            if ord(char) > 96 and ord(char) < 123:
                newname += char
                
            elif ord(char) > 64 and ord(char) < 91:
                newname += chr(ord(char)+32)
            
            elif ord(char) > 47 and ord(char) < 58:
                newname += char
                
        return newname

dict_trick_handle = { 
    'ollie' : 'ollie',
    'shoveit': 'shoveit',
    'fsshoveit': 'fsshoveit',
    'kickflip': 'kickflip',
    'heelflip' : 'heelflip',
    '360shoveit' : '360shoveit',
    'fs360shoveit' : 'fs360shoveit',
    'varialflip': 'varialflip',
    'hardflip': 'hardflip',
    'varialheelflip' : 'varialheelflip',
    'inwardheelflip' : 'inwardheelflip',
    'muskahardflip': 'muskahardflip',
    'dolphinflip': 'dolphinflip',
    'doublekickflip' : 'doublekickflip',
    'triplekickflip' : 'triplekickflip',
    'doubleheelflip' : 'doubleheelflip',
    'varialdoubleflip': 'varialdoubleflip',
    '360flip' : '360flip',
    'laserflip' : 'laserflip',
    '360hardflip' : '360hardflip',
    '540shoveit' : '540shoveit',
    'fs540shoveit' : 'fs540shoveit',
    'reversevarialflip': 'reversevarialflip',
    'wobbling360shoveit' : 'wobbling360shoveit',
    'wobblingkickflip' : 'wobblingkickflip',
    'popshoveit' : 'shoveit',
    'bsshoveit' : 'shoveit',
    'bsshuvit' : 'shoveit',
    'bspopshoveit' : 'shoveit',
    'backsideshoveit' : 'shoveit',
    'backsideshuvit' : 'shoveit',
    'backsidepopshoveit' : 'shoveit',
    'shuvit' : 'shoveit',
    'fsshuvit': 'fsshoveit',
    'fspopshoveit': 'fsshoveit',
    'frontsideshoveit': 'fsshoveit',
    'frontsideshuvit': 'fsshoveit',
    'frontsidepopshoveit': 'fsshoveit',
    '360shuvit' : '360shoveit',
    '360popshoveit' : '360shoveit',
    'bs360shoveit' : '360shoveit',
    'bs360shuvit' : '360shoveit',
    'bs360popshoveit' : '360shoveit',
    'backside360shoveit' : '360shoveit',
    'backside360shuvit' : '360shoveit',
    'backside360popshoveit' : '360shoveit',
    'varialkickflip': 'varialflip',
    'varialheel' : 'varialheelflip',
    'fs360shuvit' : 'fs360shoveit',
    'fs360popshoveit' : 'fs360shoveit',
    'frontside360shoveit' : 'fs360shoveit',
    'frontside360shuvit' : 'fs360shoveit',
    'frontside360popshoveit' : 'fs360shoveit',
    'varialdoublekickflip' : 'varialdoubleflip',
    'nightmareflip' : 'varialdoubleflip',
    '360kickflip' : '360flip',
    'treflip' : '360flip',
    '540shuvit' : '540shoveit',
    '540popshoveit' : '540shoveit',
    'bs540shoveit' : '540shoveit',
    'bs540shuvit' : '540shoveit',
    'bs540popshoveit' : '540shoveit',
    'backside540shoveit' : '540shoveit',
    'backside540shuvit' : '540shoveit',
    'backside540popshoveit' : '540shoveit',
    'fs540shuvit' : 'fs540shoveit',
    'fs540popshoveit' : 'fs540shoveit',
    'frontside540shoveit' : 'fs540shoveit',
    'frontside540shuvit' : 'fs540shoveit',
    'frontside540popshoveit' : 'fs540shoveit',
    'reversevarial': 'reversevarialflip'}

def trick_handle(cleaned_name):
    return dict_trick_handle[cleaned_name]

def reduce_name(name):

    cleaned_name = clean_name(name)

    return trick_handle(cleaned_name)
    
def reduce_deformation(trickpair):
    
    trick1 = reduce_name(trickpair[0])
    trick2 = reduce_name(trickpair[1])
    
    return (trick1, trick2)

def checkOS(osname):
    
    osname = clean_name(osname);
    
    if osname != "windows" and osname != "macos":
        raise NameError("The operating system is not valid")
    
    return osname

dict_trick_titles = { 
    'ollie' : 'Ollie',
    'kickflip': 'Kickflip',
    'varialkickflip': 'Varial Kickflip',
    'varialflip': 'Varial Flip',
    'hardflip': 'Hardflip',
    'muskahardflip': 'Muska Hardflip',
    'dolphinflip': 'Dolphin Flip',
    'shoveit' : 'Shove-it',
    'shuvit' : 'Shuvit',
    'popshoveit' : 'Pop Shove-it',
    'bsshoveit' : 'BS Shove-it',
    'bsshuvit' : 'BS Shuvit',
    'bspopshoveit' : 'BS Pop Shove-it',
    'backsideshoveit' : 'Backside Shove-it',
    'backsideshuvit' : 'Backside Shuvit',
    'backsidepopshoveit' : 'Backside Pop Shove-it',
    'fsshoveit': 'FS Shove-it',
    'fsshuvit': 'FS Shuvit',
    'fspopshoveit': 'FS Pop Shove-it',
    'frontsideshoveit': 'Frontside Shove-it',
    'frontsideshuvit': 'Frontside Shuvit',
    'frontsidepopshoveit': 'Frontside Pop Shove-it',
    'heelflip': 'Heelflip',
    'inwardheelflip': 'Inward Heelflip',
    '360shoveit': '360 Shove-it',
    '360shuvit': '360 Shuvit',
    '360popshoveit': '360 Pop Shove-it',
    'bs360shoveit': 'BS 360 Shove-it',
    'bs360shuvit': 'BS 360 Shuvit',
    'bs360popshoveit': 'BS 360 Pop Shove-it',
    'backside360shoveit': 'Backside 360 Shove-it',
    'backside360shuvit': 'Backside 360 Shuvit',
    'backside360popshoveit': 'Backside 360 Pop Shove-it',
    'fs360shoveit': 'FS 360 Shove-it',
    'fs360shuvit': 'FS 360 Shuvit',
    'fs360popshoveit': 'FS 360 Pop Shove-it',
    'frontside360shoveit': 'Frontside 360 Shove-it',
    'frontside360shuvit': 'Frontside 360 Shuvit',
    'frontside360popshoveit': 'Frontside 360 Pop Shove-it',
    'doublekickflip': 'Double Kickflip',
    'triplekickflip': 'Triple Kickflip',
    'doubleheelflip': 'Double Heelflip',
    'varialdoubleflip': 'Varial Doubleflip',
    'varialdoublekickflip': 'Varial Double Kickflip',
    'nightmareflip': 'Nightmare Flip',
    'varialheelflip': 'Varial Heelflip',
    '360flip': '360 Flip',
    '360kickflip': '360 Kickflip',
    'treflip': 'Tre Flip',
    'laserflip': 'Laser Flip',
    '360hardflip': '360 Hardflip',
    '540shoveit': '540 Shove-it',
    '540shuvit': '540 Shuvit',
    '540popshoveit': '540 Pop Shove-it',
    'bs540shoveit': 'BS 540 Shove-it',
    'bs540shuvit': 'BS 540 Shuvit',
    'bs540popshoveit': 'BS 540 Pop Shove-it',
    'backside540shoveit': 'Backside 540 Shove-it',
    'backside540shuvit': 'Backside 540 Shuvit',
    'backside540popshoveit': 'Backside 540 Pop Shove-it',
    'fs540shoveit': 'FS 540 Shove-it',
    'fs540shuvit': 'FS 540 Shuvit',
    'fs540popshoveit': 'FS 540 Pop Shove-it',
    'frontside540shoveit': 'Frontside 540 Shove-it',
    'frontside540shuvit': 'Frontside 540 Shuvit',
    'frontside540popshoveit': 'Frontside 540 Pop Shove-it',
    'reversevarialflip': 'Reverse Varialflip',
    'reversevarial': 'Reverse Varial',
    'wobbling360shoveit': 'Wobbling 360Shove-it',
    'wobblingkickflip': 'Wobbling Kickflip',
    'varialheel' : 'Varial Heel'}

def trick_title(cleaned_name):
    return dict_trick_titles[cleaned_name]

dict_def_titles = { 
    ('kickflip','heelflip'): 'From kickflip to heelflip',
    ('heelflip','kickflip'): 'From heelflip to kickflip',
    ('360shoveit','fs360shoveit'): 'From 360 shove-it to FS 360 shove-it',
    ('fs360shoveit','360shoveit'): 'From FS 360 shove-it to 360 shove-it',
    ('kickflip','360shoveit'): 'From kickflip to 360 shove-it',
    ('360shoveit','kickflip'): 'From 360 shove-it to kickflip',
    ('heelflip','360shoveit'): 'From heelflip to 360 shove-it',
    ('360shoveit','heelflip'): 'From 360 shove-it to heelflip',
    ('varialflip','540shoveit'): 'From varialflip to 540 shove-it',
    ('540shoveit','varialflip'): 'From 540 shove-it to varialflip',
    ('varialflip','inwardheelflip'): 'From varial flip to inward heelflip',
    ('inwardheelflip','varialflip'): 'From inward heelflip to varial flip',
    ('hardflip','varialheelflip'): 'From hardflip to varial heelflip',
    ('varialheelflip','hardflip'): 'From varial heelflip to hardflip',
    ('ollie','doublekickflip'): 'From ollie to double kickflip',
    ('doublekickflip','ollie'): 'From double kickflip to ollie',
    ('shoveit','varialdoubleflip'): 'From shove-it to varial doubleflip',
    ('varialdoubleflip','shoveit'): 'From varial doubleflip to shove-it',
    ('hardflip','muskahardflip'): 'From hardflip to Muska hardflip',
    ('muskahardflip','hardflip'): 'From Muska hardflip to hardflip',
    ('wobbling360shoveit','360shoveit') : 'Unwobbling 360 shove-it',
    ('wobblingkickflip','kickflip') : 'Unwobbling kickflip'}

def deformation_title(reduced_pair):
    return dict_def_titles[reduced_pair]

dict_def_handles = { 
    ('kickflip','heelflip'): 'kickflip_to_heelflip',
    ('heelflip','kickflip'): 'heelflip_to_kickflip',
    ('360shoveit','fs360shoveit'): '360shoveit_to_fs360shoveit',
    ('fs360shoveit','360shoveit'): 'fs360shoveit_to_360shoveit',
    ('kickflip','360shoveit'): 'kickflip_to_360shoveit',
    ('360shoveit','kickflip'): '360shoveit_to_kickflip',
    ('heelflip','360shoveit'): 'heelflip_to_360shoveit',
    ('360shoveit','heelflip'): '360shoveit_to_heelflip',
    ('varialflip','540shoveit'): 'varialflip_to_540shoveit',
    ('540shoveit','varialflip'): '540shoveit_to_varialflip',
    ('varialflip','inwardheelflip'): 'varialflip_to_inward_heelflip',
    ('inwardheelflip','varialflip'): 'inwardheelflip_to_varialflip',
    ('hardflip','varialheelflip'): 'hardflip_to_varialheelflip',
    ('varialheelflip','hardflip'): 'varialheelflip_to_hardflip',
    ('ollie','doublekickflip'): 'ollie_to_doublekickflip',
    ('doublekickflip','ollie'): 'doublekickflip_to_ollie',
    ('shoveit','varialdoubleflip'): 'shoveit_to_varialdoubleflip',
    ('varialdoubleflip','shoveit'): 'varialdoubleflip_to_shoveit',
    ('wobbling360shoveit','360shoveit') : 'unwobbling_360shoveit',
    ('wobblingkickflip','kickflip') : 'unwobbling_kickflip',
    ('hardflip','muskahardflip'): 'hardflip_to_muskahardflip',
    ('muskahardflip','hardflip'): 'muskahardflip_to_hardflip'}

def deformation_handle(reduced_pair):    
    return dict_def_handles[reduced_pair]