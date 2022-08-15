class Node:
  def __init__(self, isLeaf):
    self.isLeaf = isLeaf
    self.children = []
    for i in range(26):
      self.children.append(None)
      
def trieLookup(root, word):
  for x in word:
    n  = ord(x) - ord('a')
    root = root.children[n]
    if root is None: return False
    
  if root.isLeaf is True: return True 
  else: return False

def trieInsert(root,word):
    for x in word:
        n = ord(x) - ord('a')
        if root.children[n] is None:
            if x is len(word)-1:
                root.children[n] = Node(True)
            else:
                root.children[n] = Node(False)
        else:
            root = root.children[n]
            if x in len(word)-1 and root.isLeaf is True:
                root.isLeaf = False
            else:
                root.isLeaf = True
    root.isLeaf = True
     
def trieDelete(root, word, i=0): 
  if len(word)==0:
    return False
  w = word[i]
  x = ord(w) - ord('a')
  child = root.children[x]
  if child is None:
    return
  if i == len(word) - 1:
    child.isLeaf = False
  else:
    trieDelete(root,word,i+1)
  if not child.isLeaf:
    for y in child.children:
      if y is not None:
        return
    root.children[x] = None
#Autocomplete Start
def complete(root,n):
  if root.isLeaf:
    print(root.word,end=" ")
    


def Auto1()
def Auto(root,fin,n):
  for x in range(len(fin)):
    letter = ord(fin[x]) - ord('a')
    if root.children[letter] is not None:
      root = root.children[letter]
    else:
      return
  if n > 0:
    complete(root,n)
  elif n == -1:
    Auto1(root)



  
#Test Code
cont =0 
n = int(input())
comands = []
for i in range(n):
    s = input().split(" ")
    if s[0] == "insert": trieInsert(Node(False),s[1]) cont+=1
    if s[0] == "lookup": 
      if trieLookup(Node(False),s[1]): 
        print("1")
      else: 
        print("0")
    if s[0] == "remove": trieDelete(Node(False),s[1]) cont -=1
    if s[0] == "alphabetical": Alpha(Node(False))
    if s[0] == "autocomplete": Auto(Node(False),s[1],int(s[2]))
    if s[0] == "count": print(cont)
    
    
    