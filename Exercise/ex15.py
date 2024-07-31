# Write a  Python program to get the volume of a sphere with radius six.\
#   The volume of the sphere is : V = 4/3 × π × r3 = π × d3/6.


import math

radius=6.0

volume = float(4/3*math.pi*3*(radius))

print(f"The volume of sphere is {math.ceil(volume)}")