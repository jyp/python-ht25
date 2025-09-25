# Implementation of the single-rotation cellular automaton as described here:
# http://dmishin.blogspot.com/2013/11/the-single-rotation-rule-remarkably.html

# None : empty cell
# anything else: occupied

width = 80
height = 50

# rotate a 2 by 2 group at position (i,j) in grid g.
def rotate_group(g,i,j):
  save = g[i][j] # make sure this is not forgotte (overwritten in the the next line)
  g[i][j] = g[i+1][j] 
  g[i+1][j] = g[i+1][j+1]
  g[i+1][j+1] = g[i][j+1]
  g[i][j+1] = save

# indicator function of the occupied predicate.
def occupied(cell):
  if cell != None:
    return 1
  else:
    return 0

# test if there is exactly one occupied cell in the 2×2 group at position i,j in g.
def is_single_group(g,i,j):
  return occupied(g[i][j]) + occupied(g[i][j+1]) + occupied(g[i+1][j+1]) + occupied(g[i+1][j]) == 1

def rotate_all_groups(offset,g):
  # ATTENTION! we remove one from the higher bounds because we need to
  # access two elements. (The range function already removes one.)
  for i in range(offset,height-1,2):
    for j in range(offset,width-1,2):
      # here (i,j) is the top-left corner of each group
      if is_single_group(g,i,j):
        rotate_group(g,i,j)

def make_glider(g,i,j,o):
  g[i][j] = o
  g[i][j+1] = o
  g[i+2][j] = o
  g[i+2][j+1] = o

def make_wall(g,i,j,h,o):
  for k in range(i,i+h):
    g[k][j] = o
    g[k][j+1] = o

def display(g):
  print("\033[1;1H") # terminal command to go to top left of screen.
  for row in g:
    for cell in row:
      if cell == None:
        print(" ", end="")
        # the end="" parameter means to not print a newline. (this way
        # all the cells in the row will be displayed on the same line)
      else:
        print(cell, end="")
    print()

# make empty grid
grid=[]
for i in range(height):
  grid.append([ None ] * width)

  
make_glider(grid,4,5,'o')
make_wall(grid,7,15,12,"#")

for i in range(10000):
  display(grid)
  # input()
  rotate_all_groups(i % 2,grid)



















