"""
Created on Wed May 20 2021
Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
"""
import sympy as sm
import SkateTrick as st
import matrixTricks
import misc


print('Welcome to Topological Flips')

main_loop = True;

while main_loop:
    # First Interaction
    first_interaction = True
    while first_interaction:
        print('\nEnter a skatetrick: ')
        print('(If you would like to see a list of available tricks, enter \"list tricks\")')
        first_input = input()
    
        if first_input == "list tricks":
            for i in matrixTricks.tricks.keys():
                print(i)
        else:
            first_input = st.clean_name(first_input)
            trick = st.SkateTrick(first_input)
            first_interaction = False
    
    # Second Interaction
    print('\nOptions are:')
    print('1 -> Print rotational matrix.')
    print('2 -> Produce animation of skate trick.\n')
    
    user_input = input('Enter the desired option: ')
    
    
    if user_input == '1':
        # Command to print rotational matrix
        sm.pprint(trick.matrix)
    
    #print('NowWill now render the', user_input)
    
    if user_input == '2':
        print('Which operating system are you using?')
        print('1 -> OSX')
        print('2 -> Windows')
        os_input = input('Enter the desired option: ')
        
        if os_input == "1":
            os = "osx";
        if os_input == "2":
            os = "windows";
            
        print('Which file type would you like?')
        print('1 -> mp4')
        print('2 -> GIF')
        ft_input = input('Enter the desired option: ')
        
        if ft_input == "1":
            file_type = ".mp4";
        if ft_input == "2":
            file_type = ".gif";
            
        trick.create_animation(os,file_type)
    
        print('The animation is located in the flipgifs directory.')
    
    last_question = True;
    while last_question:
        
        print("Would you like to quit the program?")
        user_input = input('Enter Y/N: ')
        
        user_input = misc.clean_name(user_input);
            
        if user_input == "y" or user_input == "yes":
            last_question = False;
            main_loop = False;
            
        elif user_input == "n" or user_input == "no":
            last_question = False;
        
        else:
            print("Invalid response.")
    