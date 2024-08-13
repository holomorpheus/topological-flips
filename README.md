# Topological Flips  

A script which can create animations and spherical plots of different skate tricks and homotopies between them.

Author:  
Gabriel Martins (@holomorpheus)  

Contributors:  
José Bravo (@jbravo87), Robert Hingtgen, Justus Carlisle  

__Necessary Applications__

- Python 3  
- Numpy, Sympy and Matplotlib libraries  
- FFmpeg

__How to use__

In order to use this program:  

1) Clone the repository into a local directory.
2) Run the script `main.py`.
3) You may now use the main functions in the package to create spherical plots or animations of different flip tricks and homotopies between them. Please see the examples below.

__Using the main functions in the package__

All currently available flip tricks can be displayed by running:
```python
list_fliptricks()
```

If one would like to see all available flip tricks including alternate spellings for a variety of tricks, one may do so by running:
```python
list_fliptricks(complete = True)
```

All currently available homotopies can be displayed by running:
```python
list_homotopies()
```

In order to create a spherical plot of a varial kickflip, you main run:
```python
sphere_flip_plot('varialkickflip')
```

In order to create a spherical plot of a homotopy between a double kickflip and an ollie, you main run:
```python
sphere_homotopy_plot(('varialkickflip','inwardheelflip'))
```

In order to create an mp4 video of a varial kickflip, you main run:
```python
animate_fliptrick('varialkickflip')
```

In order to create an mp4 video of a homotopy between a double kickflip and an ollie, you main run:
```python
animate_homotopy(('ollie','doublekickflip'))
```
