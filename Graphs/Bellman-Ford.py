class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node, weight):
    self.neighbors.append((another_node, weight))
    
def bellman_ford(graph, source):
    dist = {}
    for sources in range(len(graph)):
        if graph[sources] == source:
            dist[graph[sources]] = 0
        else:
            dist[graph[sources]] = float('inf')
    for number in range(len(graph)-1):
        for node in graph:
            for edge in node.neighbors:
                if dist[node] + edge[1] < dist[edge[0]]:
                    dist[edge[0]] = dist[node] + edge[1]
    resultados = []
    for x in graph:
        resultados.append(dist[x])
    return resultados


# Test Code  
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.connect(c, 8)
a.connect(f, -3)

b.connect(c, 2)
b.connect(e, -5)

c.connect(d, 3)

d.connect(a, 12)
d.connect(f, 9)

e.connect(a, 4)

f.connect(b, 6)

g = [a, b, c, d, e, f]

print(bellman_ford(g,f)) # should return [5, 6, 8, 11, 1, 0]