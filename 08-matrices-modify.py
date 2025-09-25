
# None : empty cell
# anything else: occupied

width = 80
height = 50

def rotate_group(g,i,j):
  save = g[i][j]
  g[i][j] = g[i+1][j] 
  g[i+1][j] = g[i+1][j+1]
  g[i+1][j+1] = g[i][j+1]
  g[i][j+1] = save

def occupied(cell):
  return cell != None

def is_single_group(g,i,j):
  return occupied(g[i][j]) + occupied(g[i][j+1]) + occupied(g[i+1][j+1]) + occupied(g[i+1][j]) == 1

def rotate_all_groups(offset,g):
  for i in range(offset,height-1,2):
    for j in range(offset,width-1,2):
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
  print("\033[1;1H")
  for row in g:
    for cell in row:
      if cell == None:
        print(" ", end="")
      else:
        print(cell, end="")
    print()

grid=[]
for i in range(height):
  grid.append([ None ] * width)

  
make_glider(grid,4,5,'o')
make_wall(grid,7,15,12,"#")

for i in range(10000):
  display(grid)
  # input()
  rotate_all_groups(i % 2,grid)



















