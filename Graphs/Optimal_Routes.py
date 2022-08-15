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
results = {}
inicio = input()
nodes.append(Node(inicio))
text.append(inicio)
n = int(input())
for x in range(n):
    s = input().split(", ")
    nodes.append(Node(s[0]))
    results[s[0]]=int(s[1])
    places.append(s[0])
    text.append(s[0])
    
e = int(input())
for j in range(e):
    s = input().split(", ")
    n1 = Find(nodes,s[0])
    n2 = Find(nodes,s[1])
    if n1 is None:
        n1 = Node(s[0])
        nodes.append(n1)
    if n2 is None:
        n2 = Node(s[1])
        nodes.append(n2)
    n1.connect(n2,int(s[2]))
    
places = sorted(places,key=str.lower)
graph = to_matrix(nodes)

for n in places:
    s = ""
    no=nodes.index(Find(nodes,n))
    matresult=graph[0][no]
    s += n
    if matresult==results[n]:
        s+=" YES"
    else:
        s+=" NO"
    print(s)
    
    


    