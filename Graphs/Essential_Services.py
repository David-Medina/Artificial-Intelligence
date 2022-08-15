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


#input 
nodes = []
places = []
names=[]
text=[]
n = int(input())
for x in range(n):
    s = input()
    nodes.append(Node(s))
    names.append(s)
    text.append(s)
    
p = int(input())
for y in range(p):
    s= input()
    nodes.append(Node(s))
    places.append(s)
    text.append(s)
e = int(input())
for j in range(e):
    s = input().split(", ")
    n1 = Find(nodes,s[0])
    n2 = Find(nodes,s[1])
    n1.connect(n2,int(s[2]))
    
places = sorted(places)
names = sorted(names)
graph = to_matrix(nodes)

print(' '.join(places))
for n in names:
    s = ""
    personInd=text.index(n)
    for loc in places:
        locInd=text.index(loc)
        s+=str(graph[locInd][personInd])+" "
    s+=str(n)
    print(s)
    


    
    
    