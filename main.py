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
    first_interaction = True;
    
    while first_interaction:
        
        print('\nPlease choose a skate trick: ')
        print('\nIf you would like to see a list of available tricks, type \"list\".')
        
        user_input = input("Enter your response: ");
        user_input = misc.clean_name(user_input);
        
        if user_input == "list":
            print("\nThese are the available tricks in the collection:\n")
            for i in matrixTricks.plot_titles.values():
                print(i)
        else:
            try:
                trick = st.SkateTrick(user_input);
                first_interaction = False
            except KeyError:
                print("\nInvalid response. Please try again.")
    
    # Second Interaction
    second_interaction = True;
    first_pass = True;
    
    while second_interaction:
        
        if first_pass:
            print('\nYour options are:')
            print('1 -> Print rotation matrix.')
            print('2 -> Generate an animation for the skate trick.\n')
            
            user_input = input('Enter the desired option: ')
            user_input = misc.clean_name(user_input);
            
        # Print rotation matrix
        if user_input == '1':
            print("")
            sm.pprint(trick.matrix)
            
            second_option = True;
                
            while second_option:
                
                print("\nWould you like to generate an animation for this trick?")
                
                user_input = input('Enter Y/N: ')
                user_input = misc.clean_name(user_input);
                
                if user_input == "y" or user_input == "yes":
                    second_option = False;
                    first_pass = False;
                    user_input = '2';
                    
                elif user_input == "n" or user_input == "no":
                    second_option = False;
                    second_interaction = False;
                
                else:
                    print("\nInvalid response.")     
        
        # Create animation
        elif user_input == '2':
            print('\nWhich operating system are you using?')
            print('1 -> macOS')
            print('2 -> Windows')
            os_input = input('Enter the desired option: ');
            os_input = misc.clean_name(os_input);
            
            if os_input == "1":
                os = "macos";
            if os_input == "2":
                os = "windows";
                
            print('\nWhich file type would you like?')
            print('1 -> mp4')
            print('2 -> GIF')
            ft_input = input('Enter the desired option: ')
            
            if ft_input == "1":
                file_type = ".mp4";
            if ft_input == "2":
                file_type = ".gif";
                
            print("\nThis will take a minute or two...")    
            trick.animate(os,file_type)
        
            print('\nThe animation is located in the animation directory.')
            
            second_option = True;
                
            while second_option:
                
                print("\nWould you like to print a rotation matrix for this trick?")
                
                user_input = input('Enter Y/N: ')
                user_input = misc.clean_name(user_input);
                
                if user_input == "y" or user_input == "yes":
                    second_option = False;
                    first_pass = False;
                    user_input = '1';
                    
                elif user_input == "n" or user_input == "no":
                    second_option = False;
                    second_interaction = False;
                
                else:
                    print("\nInvalid response.") 
    
    last_question = True;
    
    while last_question:
        
        print("\nWould you like to quit the program?")
        user_input = input('Enter Y/N: ')
        
        user_input = misc.clean_name(user_input);
            
        if user_input == "y" or user_input == "yes":
            last_question = False;
            main_loop = False;
            
        elif user_input == "n" or user_input == "no":
            last_question = False;
        
        else:
            print("\nInvalid response.")
    