import sys, pygame
from pygame.locals import *
from pygame.gfxdraw import filled_polygon
from time import sleep
hexgrid_width = 50
hexgrid_height = 50

ALIVE = RED = (255, 0, 0)
DEAD = BLACK = (0,0,0)

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
##########################

import numpy as np
survival = [0, 3, 4, 5]
def hexlifeGenerator(w, h, initial = None):
  if initial == None:
    state = np.zeros(shape = (h,w), dtype = bool)
    state[h//2][w//2] = 1
  else:
    state = initial
  while 1:
    yield state
    lastState = np.copy(state)
    for row in range(h):
      for col in range(w):
        livingNeighborsCount=0+lastState[row%h][(col + 1)%w] + lastState[row%h][(col - 1)%w]+\
                          lastState[(row - 1)%h][col%w] + lastState[(row + 1)%h][col%w]+\
                          lastState[(row + 1)%h][(col - 1)%w] + lastState[(row - 1)%h][(col + 1)%w]
        state[row][col] = livingNeighborsCount in survival


#########################
def render(display, state):
    for row in range(-1, hexgrid_height+1):
        for col in range(-row, hexgrid_width+1):
            color = ALIVE if state[row%hexgrid_width][col%hexgrid_height] else DEAD
            hexcenter = hexagon_coordinates(row, col)
            points = hexagon_vertices(hexcenter)
            filled_polygon(display, points, color)
    
g = hexlifeGenerator(50, 50)
def main():
  pygame.init()
  
  DISPLAY = pygame.display.set_mode((int(hexgrid_width * inradius*2), int(hexgrid_height*exradius*1.5)), 0, 32)

  WHITE = (255, 255, 255)
  BLUE = (0, 0, 255)

  DISPLAY.fill(WHITE)
  
  for state in g:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    sleep(0.25)
    
    render(DISPLAY, state)
    
    pygame.display.update()
main()


