n = int(input())
grid = []
for x in range(n):
    grid.append(input().split(" "))
    
dic = {}
def sumar(grid,cord):
    if cord in dic: return dic[cord]
    if cord[0] >= len(grid):
        dic[cord]=0
        return 0
    if cord[1] >= len(grid):
        dic[cord]=0
        return 0
    if grid[cord[0]][cord[1]]=='1': 
        dic[cord]=0
        sumar(grid,(cord[0],cord[1]+1))
        sumar(grid,(cord[0]+1,cord[1]+1))
        sumar(grid,(cord[0]+1,cord[1]))
        return 0
    dic[cord]=min(sumar(grid,(cord[0],cord[1]+1)),sumar(grid,(cord[0]+1,cord[1]+1)),sumar(grid,(cord[0]+1,cord[1])))+1
    return dic[cord]
    
sumar(grid,(0,0))       
maxs=0
for i in range(n):
    for j in range(n):
        maxs=max(dic[(i,j)],maxs)    
print(maxs)
    