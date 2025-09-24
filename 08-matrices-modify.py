

def display(m):
  print("\033[1;1H")
  print("vvvvvvvv")
  for row in m:
    print(">",end="")
    for x in row:
        print(x or " ", end="")
    print("<")
  print("^^^^^^^^^")

