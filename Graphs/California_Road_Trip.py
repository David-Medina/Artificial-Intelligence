class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node):
    self.neighbors.append(another_node)
    another_node.neighbors.append(self)
  
def DFS(graph,deph,start):
  visited = set()
  results = []
  for node in graph:
    if node.value == start:
        dfs_helper(node, visited, results,deph)
  return sorted(results)

def dfs_helper(start, visited, results,deph):
  # if we have already visited this node, we should return
  # since we don't want to visit a node twice
  if start in visited or deph < 0:
    return
  # do the work for this node (i.e. append it to `results`)
  results.append(start.value)
  # add this node to the set of visited nodes
  visited.add(start)
  # loop over all the neighbors of this node, and recursively call
  for x in start.neighbors:
    dfs_helper(x,visited,results,deph-1)
  # this function on each of them

#input
arr = []
conx = []
n = int(input())
location = str(input())
k = int(input())
for places in range(len(k)):
    s = input().split(": ")
    conx.append(s[1].split(", "))
    arr.append(Node(s[0]))
for i in range(len(k)):
    for x in conx:
        for j in range(len(k)):
            if x == arr[j].value:           
                if arr[j] not in arr[i].neighbors:
                    arr[i].connect(arr[j])


print(DFS(arr,n,location))   
    


