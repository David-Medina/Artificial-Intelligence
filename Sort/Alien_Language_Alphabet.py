import queue
class Node:
  def __init__(self, value):
    self.value = value
    self.neighbors = []
    self.in_degree = 0
    
  def connect(self, another_node):
    self.neighbors.append(another_node)

def calculate_in_degree(graph):
  for node in graph:
    for n in node.neighbors:
      n.in_degree +=1
  
def kahns_algo(graph):
  calculate_in_degree(graph)
  d = queue.Queue()
  res = []
  for node in graph:
    if node.in_degree == 0:
      d.put(node)
  while not d.empty():
    temp = d.get()
    res.append(temp.value)
    for i in temp.neighbors:
      i.in_degree -=1
      if i.in_degree == 0 and i.value not in res:
        d.put(i)
        
  return res


def find(arr,char):
    for x in arr:
        if x.value == char:
            return x
    return None

def compare(w1,w2, i):
    
    if w1[i] == w2[i]:
            return compare(w1,w2,i+1)
    return w1[i],w2[i]
    
    
#input
arr = []
words = []
letras= []
n = int(input())
for x in range(n):
    s = input()
    words.append(s)
for a in words:
    for letter in a:
        if letter not in letras:
            letras.append(letter)
for i in letras:
    arr.append(Node(i))
    

for x in range(len(words)-1):
    char1,char2 = compare(words[x],words[x+1],0)
    if char2 is not None:
        n1 = find(arr,char1)
        n2 = find(arr,char2)
        n1.connect(n2)
        
    


r =kahns_algo(arr)
print(' '.join(r))

        
            


    