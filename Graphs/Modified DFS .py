class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    self.visit = False
    
  def connect(self, another_node):
    self.neighbors.append(another_node)

def dfs_sorting(graph):
    stack = []
    for node in graph:
        dfs_helper(node,stack)
    return list(reversed(stack))
    

def dfs_helper(start,stack):
  # if we have already visited this node, we should return
  # since we don't want to visit a node twice
  if start.visit is True:
    return
  # do the work for this node (i.e. append it to `results`)
  # add this node to the set of visited nodes
  start.visit = True
  # loop over all the neighbors of this node, and recursively call
  for x in start.neighbors:
    dfs_helper(x,stack)
  stack.append(start.value)

  # this function on each of them
    
  

# Test Code
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

a.connect(b)
a.connect(d)

c.connect(d)
c.connect(g)
c.connect(h)

d.connect(g)

h.connect(e)
h.connect(f)

graph = [a, b, c, d, e, f, g, h]

print(dfs_sorting(graph)) # should print [C, H, F, E, A, D, G, B]