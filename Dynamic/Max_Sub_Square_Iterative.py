n = int(input())
grid = []
for x in range(n):
    grid.append(input().split(" "))
    
def sumar(grid,cord):
    dic=[]
    for i in range(len(grid)):
        dic.append([0]*len(grid))
    maximo = 0
    for x in range(len(grid)-1,-1,-1):
        for y in range(len(grid)-1,-1,-1):
            if grid[x][y] == '1':
                dic[x][y]=0
            else:
                der = 0
                abajo = 0
                diag = 0 
                if x < len(grid)-1:
                    der = dic[x+1][y]
                if y < len(grid)-1:
                    abajo = dic[x][y+1]
                if y < len(grid)-1 and x < len(grid)-1:
                    diag = dic[x+1][y+1]
                dic[x][y] = 1+min(der,abajo,diag)
                if dic[x][y] > maximo:
                    maximo = dic[x][y]
    return maximo

print(sumar(grid,(0,0)))


            