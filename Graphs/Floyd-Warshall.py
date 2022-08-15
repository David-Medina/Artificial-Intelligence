class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node, weight):
    self.neighbors.append((another_node, weight))


def to_matrix(graph):
    matrix = []
    for i in range(len(graph)):
        matrix.append([])
        for j in range(len(graph)):
            matrix[i].append(float('inf'))
        matrix[i][i] = 0
    #put te weight in the matrix
    for node in graph:
        for edge in node.neighbors:
            neighbor = edge[0]
            weight = edge[1]
            i = graph.index(node)
            j = graph.index(neighbor)
            matrix[i][j] = weight
    #now floyd_warshall
    for k in range(len(graph)):
        for j in range(len(graph)):
            for i in range(len(graph)):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix 

# Test Code  
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.connect(c, 5)
c.connect(a, 5)

b.connect(c, 2)
c.connect(b, 2)

b.connect(d, 1)
d.connect(b, 1)

c.connect(d, -3)
g = [a, b, c, d]

print(to_matrix(g)) 
