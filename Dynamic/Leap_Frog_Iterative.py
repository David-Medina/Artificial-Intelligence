import math 
def leap_frog(stair):
    linus = [0]*len(stair)
    for y in range(len(stair)-1,-1,-1):
        if stair[y]==0:
            linus[y]=math.inf
        else: 
            mini = math.inf
            for x in range(0,stair[y]):
                if x+1+y > len(stair)-1: 
                    mini=0
                else: 
                    mini = min(linus[x+1+y],mini)
            linus[y] = mini + 1
    

    return linus[0] 

                
n = int(input())
valor = input().split(" ")

l=[]
for i in valor:
    l.append(int(i))
result=leap_frog(l)
if result== math.inf: 
    print(-1)
else:
    print(leap_frog(l))
           