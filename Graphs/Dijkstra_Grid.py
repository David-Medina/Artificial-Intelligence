import math
class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node, weight):
    self.neighbors.append((another_node, weight))
    another_node.neighbors.append((self, weight))

def Find(graph,coord):
  for n in graph:
    if n.value == coord:
      return n
  return None

def cuatro(graph):
  for node in graph:
    x,y = node.value
    vecino = Find(graph,(x+1,y))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x-1,y))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x,y-1))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x,y+1))
    if vecino is not None:
      node.connect(vecino,1)
  return graph

def ocho(graph):
  for node in graph:
    x,y = node.value
    vecino = Find(graph,(x+1,y))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x-1,y))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x+1,y+1))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x-1,y+1))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x+1,y-1))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x-1,y-1))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x,y+1))
    if vecino is not None:
      node.connect(vecino,1)
    vecino = Find(graph,(x,y-1))
    if vecino is not None:
      node.connect(vecino,1)
  return graph

def find_min(distances, finalized):
  # distances is a dictionary of node => shortest distance so far to that node
  # finalized is a set of nodes for which distances has been finzlied
  # TODO
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


dimension = int(input())
start = input().split(" ")
end = input().split(" ")
mov = int(input())
arr = []
for a in range(dimension):
  arr.append(input().split(" "))

graph = []
for x in range(dimension):
  for y in range(dimension):
    if arr[x][y] == 'O':
      graph.append(Node((x,y)))
if mov == 4:
  graph = cuatro(graph)
else:
  graph = ocho(graph)

print(dijkstra(graph,Find(graph,(int(start[0]),int(start[1]))),Find(graph,(int(end[0]),int(end[1])))))




