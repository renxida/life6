import numpy as np
default_survival_condition = [0, 3, 4, 5]

class hexlife_iterator:
    def __init__(self, grid_height, grid_width, rule = default_survival_condition, initial_state = None):
        """
        rule: survival condition. list of number of live neighbors required for a
        cell to survive. numbers are between 0 and 6 inclusive. Suggests including 0
        and excluding 6 to get interesting patterns that keep running for a long time
        """
        self.grid_height = grid_height
        self.grid_width  = grid_width
        self.rule = rule
        if initial_state == None:
            self.initial_state = np.zeros(shape = (self.grid_height, self.grid_width),
                                          dtype = bool)
            self.initial_state[grid_height//2][grid_width//2] = 1
        else:
            self.inital_state = initial_state
        self.state = self.initial_state
        
    def __iter__(self):
        """
        creates iterator from set parametrs and returns it
        uses python yield synax
        which is the best thing ever
        if you say otherwise i'll cover my ears
        and yell at the top of my voice
        """
        while 1:
            yield self.state
            lastState = np.copy(self.state)
            for row in range(self.grid_height):
                for col in range(self.grid_width):
                    livingNeighborsCount=0+lastState[row%self.grid_height][(col + 1)%self.grid_width] + lastState[row%self.grid_height][(col - 1)%self.grid_width]+\
                        lastState[(row - 1)%self.grid_height][col%self.grid_width] + lastState[(row + 1)%self.grid_height][col%self.grid_width]+\
                        lastState[(row + 1)%self.grid_height][(col - 1)%self.grid_width] + lastState[(row - 1)%self.grid_height][(col + 1)%self.grid_width]
                    self.state[row][col] = livingNeighborsCount in self.rule