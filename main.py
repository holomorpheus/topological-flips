"""
Created on Wed May 20 2021

Authors:
    Gabriel Martins (@holomorpheus)
    José Bravo (@jbravo87)
"""
import sympy as sm
import SkateTrick as st
import matrixModule

print('Welcome to Topological Flips')

first_interaction = True
while first_interaction:
    print('\nEnter a skatetrick: ')
    print('(If you would like to see a list of available tricks, enter \"list tricks\")')
    first_input = input()

    if first_input == "list tricks":
        for i in matrixModule.tricks.keys():
            print(i)
    else:
        trick = st.SkateTrick(first_input)
        first_interaction = False

print('\nOptions are\n 1 -> Print rotational matrix.\n 2 -> Produce animation of stunt.\n')

user_input = input('Enter the desired option: ')


if user_input == '1':
    # Command to print rotational matrix
    sm.pprint(trick.matrix)

#print('NowWill now render the', user_input)

if user_input == '2':
    trick.create_gif()

print('The GIf is located in the flipgifs directory.')
