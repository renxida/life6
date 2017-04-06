import numpy as np
default_survival_condition = [0, 3, 4, 5]

def hexlife_generator(h, w, rule = default_survival_condition, initial_state = None):
  """
  rule: survival condition. list of number of live neighbors required for a
  cell to survive. numbers are between 0 and 6 inclusive. Suggests including 0
  and excluding 6 to get interesting patterns that keep running for a long time
  """
  if initial_state == None:
    state = np.zeros(shape = (h,w), dtype = bool)
    state[h//2][w//2] = 1
  else:
    state = initial_state
  while 1:
    yield state
    lastState = np.copy(state)
    for row in range(h):
      for col in range(w):
        livingNeighborsCount=0+lastState[row%h][(col + 1)%w] + lastState[row%h][(col - 1)%w]+\
                          lastState[(row - 1)%h][col%w] + lastState[(row + 1)%h][col%w]+\
                          lastState[(row + 1)%h][(col - 1)%w] + lastState[(row - 1)%h][(col + 1)%w]
        state[row][col] = livingNeighborsCount in rule