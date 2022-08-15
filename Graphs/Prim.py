class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node, weight):
    self.neighbors.append((another_node, weight))
    another_node.neighbors.append((self, weight))
    
def prim(graph):
    minimunm = set()
    map_of_nodes =  {}
    for x in range(len(graph)):
        map_of_nodes[x] = (None,float('inf'))

# Test Code  
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.connect(g, 1)
a.connect(b, 3)
a.connect(f, 5)

b.connect(d, 6)
b.connect(e, 9)

c.connect(d, 4)
c.connect(g, 14)

d.connect(g, 18)
e.connect(g, 11)

graph = [a, b, c, d, e, f, g]

print(prim(graph)) # should return [(a,g), (a,b), (a,f), (b,d), (d,c), (b,e)]