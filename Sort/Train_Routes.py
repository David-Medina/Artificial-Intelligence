import queue
class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    
  def connect(self, another_node):
    self.neighbors.append(another_node)
    another_node.neighbors.append(self)
  
def BFS(graph):
  cont =0
  visited = set()
  results = []
  for node in graph:
    if node not in visited:
        bfs_helper(node, visited, results)
        cont +=1
  return cont

def bfs_helper(start, visited, results):
  # if we have already visited this node, we should return since we don't
  # want to visit a node twice
  if start in visited:
    return 
  # add the current node to the `visited` set
  visited.add(start)
  # start an empty queue, and add `start` to it
  l = queue.Queue()
  l.put(start)
  # write a while loop that will run as long the queue has items
  while not l.empty():
    # pop the next node from the queue
    node = l.get()
    # do the work for this node (i.e. append it to `results`)
    results.append(node.value)
    # loop over all the neighbors of this node
    for x in node.neighbors:
      # if the current neighbor hasn't been visited yet
      if x  not in visited:
        # add this neighbor to the queue
        l.put(x)
        # add this neighbor to the set of visited nodes
        visited.add(x)

#input
arr = []
conx = []
n = int(input())
for x in range(n):
    s = input().split(": ")
    conx.append(s[1].split(", "))
    arr.append(Node(s[0]))

for i in range(n):
    for x in conx[i]:
        for j in range(n):
            if x == arr[j].value:
                if arr[j] not in arr[i].neighbors:
                    arr[i].connect(arr[j])
print(BFS(arr))