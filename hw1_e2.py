#hw1_e2.py by mohammed - estimating pi/4

import math
import random

random.seed(1) # Fixes the seed of the random number generator.

# Function to generate random float
def rand():
    return random.uniform(-1, 1)
    
# Function to calculate distance between point and origin
def distance(x, origin):
    return math.sqrt((x[0] - origin[0])**2 + (x[1] - origin[1])**2)

# Function will determine if point is in circle
def in_circle(x, origin = [0,0]):
   return distance(x, origin) < 1

R=10000 # num of random points

inside = [in_circle([rand(), rand()]) for i in range (R)]

proportion = sum(inside) / R # sum(inside) automatically counts True because True is 1

print(proportion)
   
print(math.pi / 4)

print((math.pi / 4) - proportion)
