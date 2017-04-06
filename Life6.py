import sys, pygame
from pygame.locals import *
from pygame.gfxdraw import filled_polygon
from time import sleep

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
ALIVE, DEAD = RED, BLACK

from hexagon_grid import hexagon_vertices, hexagon_coordinates, inradius, exradius
from hexlife_iterator import hexlife_iterator

def render(display, state, hexgrid_height, hexgrid_width):
    for row in range(-1, hexgrid_height+1):
        for col in range(-row, hexgrid_width+1):
            color = ALIVE if state[row%hexgrid_height][col%hexgrid_width] else DEAD
            hexcenter = hexagon_coordinates(row, col)
            points = hexagon_vertices(hexcenter)
            filled_polygon(display, points, color)
    
it = hexlife_iterator(15, 19)

def main():
  pygame.init()

  DISPLAY = pygame.display.set_mode((int(it.grid_width * inradius*2), int(it.grid_height*exradius*1.5)), 0, 32)

  DISPLAY.fill(WHITE)
  
  for state in it:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    sleep(0.25)
    
    render(DISPLAY, state, it.grid_height, it.grid_width)
    
    pygame.display.update()
if __name__ == "__main__":
    main()
