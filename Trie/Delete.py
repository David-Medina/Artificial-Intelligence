class Node:
  def __init__(self, isLeaf):
    self.isLeaf = isLeaf
    self.children = []
    for i in range(26):
      self.children.append(None)
      
def trieDelete(root, word, i=0): 
  w = word[i]
  x = ord(w) - ord('a')
  child = root.children[x]
  if child is None: 
    return 
  if i == len(word) - 1:
    child.isLeaf = False
  else:
    child.isLeaf = None
    root.children[x] = None
    trieDelete(root,word,i+1)
  if not child.isLeaf:
    for y in child.children:
      if y is None:
        return
      else:
    root.children[x] = None
