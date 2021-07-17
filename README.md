# Seed-Disposition-Golden-Angle
Simulation of the natural disposition of seeds on sunflowers utilising the Golden Angle

## Explanation:

In nature, the phyllotaxis of plants are quite interesting.


In most cases, at the exception of rare occasions (like clovers), flowers and plants will have a certain number of petals or leaves per knot.


And it just so happens that it corresponds to a term in the Fibonacci sequences (0, 1, 1, 2, 3, 5, 8, 13, 21...)


The disposition of seeds on a sunflower uses an identical method, by rotating each seed around a center (in this case: the center of the sunflower) using the Golden Angle.


The Golden Angle is calculated by multiplying (3 - sqrt(5)) by 180, giving us an angle of roughly 137.5°.


This number is then used to angle each seed around the center of the sunflower, and its distance will perform an outwards motion (increasing distance from the center), thus obtaining a very similar disposition of how sunflower seeds are positioned naturally.


## Controls:

[Escape] -> Take screenshot (Saved to /screenshots/)


## Installation information:

A "requirements" text file is provided within the repository.


To install the necessary library(ies) to run the script:

1- Open CMD or GitBash


2- Change the current directory to the project path (cd path\\to\\project)


3- Install the library(ies) from the "requirements.txt" file (pip install -r requirements.txt)


## Development information:

Developed by: SammygoodTunes


Library(ies) used: Pygame 2.0.1
