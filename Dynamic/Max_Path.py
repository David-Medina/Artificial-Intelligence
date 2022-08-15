# initialize an empty dictionary
res = {}
def maxPath(arr, r, c):
  if (r,c) in res:  # if r, c are in the dictionary, return 
    return res[(r,c)]
  if r == len(arr)-1 and c == len(arr)-1: # if this is the last cell in the grid (i.e. bottom-right corner
    return arr[r][c]  #simply return its value
  if r == len(arr)-1: # if r is last row
    value = maxPath(arr,r,c+1)   #   compute the value of the max_path going straight right
  elif c == len(arr)-1:  # else if c is last column
    value = maxPath(arr,r+1,c) #   compute the value of the max_path going straight down
  else: # else
    value = max(maxPath(arr,r+1,c),maxPath(arr,r,c+1)) #pick the max of maxPath(r, c + 1) and maxPath(r + 1, c)
  res[(r,c)] = value + arr[r][c] # store the maxPath + value of current cell in dictionary
  # return it
  return res[(r,c)]



arr = [
 [1, 2, 3, 2],
 [3, 1, 9, 3],
 [4, 2, 5, 1],
 [1, 3, 4, 3],
]
print(maxPath(arr, 0, 0)) # should print 27