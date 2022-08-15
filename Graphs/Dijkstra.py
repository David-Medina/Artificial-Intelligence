import math
class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node, weight):
    self.neighbors.append((another_node, weight))
    another_node.neighbors.append((self, weight))


def find_min(distances, finalized):
  minSoFar = None
  for node in distances:
    if node in finalized: continue
    if minSoFar is None or distances[node] < distances[minSoFar]:
      minSoFar = node
  return minSoFar

def dijkstra(graph, source, destination):
  distances = {}
  for x in graph:
    if x == source:
      distances[x] = 0
    else: 
      distances[x] = math.inf
  finalized = set()
  node = source
  while node is not destination:
    node = find_min(distances,finalized)
    finalized.add(node)
    if distances[node] is not math.inf:
      for v in node.neighbors:
        d = v[1] + distances[node]
        if d < distances[v[0]]:
          distances[v[0]] = d 
  
  return distances[destination]   
        
        
    
    
    
    
# Test code

a = Node("A")
b = Node("B")
b.connect(a, 3)

c = Node("C")
c.connect(b, 5)

d = Node("D")
d.connect(a, 3)

e = Node("E")
e.connect(c, 7)

f = Node("F")
f.connect(d, 7)
f.connect(c, 4)

g = Node("G")
g.connect(f, 8)
g.connect(a, 1)

h = Node("H")
h.connect(c, 1)
h.connect(f, 1)
h.connect(g, 4)
graph = [a, b, c, d, e, f, g, h]

print(dijkstra(graph, a, f)) # should print 6
print(dijkstra(graph, a, e)) # should print 13