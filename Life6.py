import sys, pygame
from pygame.locals import *
from pygame.gfxdraw import filled_polygon
from time import sleep
hexgrid_width = 50
hexgrid_height = 50

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
ALIVE, DEAD = RED, BLACK

from hexagon_grid import hexagon_vertices, hexagon_coordinates, inradius, exradius
from hexlife_generator import hexlife_generator

def render(display, state):
    for row in range(-1, hexgrid_height+1):
        for col in range(-row, hexgrid_width+1):
            color = ALIVE if state[row%hexgrid_width][col%hexgrid_height] else DEAD
            hexcenter = hexagon_coordinates(row, col)
            points = hexagon_vertices(hexcenter)
            filled_polygon(display, points, color)
    
g = hexlife_generator(50, 50)

def main():
  pygame.init()

  DISPLAY = pygame.display.set_mode((int(hexgrid_width * inradius*2), int(hexgrid_height*exradius*1.5)), 0, 32)

  DISPLAY.fill(WHITE)
  
  for state in g:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    sleep(0.25)
    
    render(DISPLAY, state)
    
    pygame.display.update()
if __name__ == "__main__":
    main()