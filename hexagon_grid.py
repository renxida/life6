import numpy as np
PI = np.pi
TAU = 2*PI
from math import sqrt
exradius = 10
inradius = exradius * (sqrt(3)/2.0)
angles = (np.array((0,1,2,3,4,5))/6) * TAU
yoffset = exradius * np.cos(angles)
xoffset = exradius * np.sin(angles)
def hexagon_vertices(center):
  center = np.array(center)
  pointsx = xoffset + center[0]
  pointsy = yoffset + center[1]
  return np.array((pointsx, pointsy)).T

def hexagon_coordinates(r, c):
    return ((c+r*0.5)*inradius*2,r*1.5*exradius)