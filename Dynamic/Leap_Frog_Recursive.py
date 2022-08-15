import math
linus = {}
def leap_frog(stair,step):
    if step >= len(stair):
        return 0
    if stair[step]==0: 
        return math.inf
    else: 
        mini = math.inf
        for x in range(stair[step]):
            mini = min(leap_frog(stair,step+x+1),mini)
        linus[step]=mini+1
    return linus[step]

n = int(input())
valor = input().split(" ")

l=[]
for i in valor:
    l.append(int(i))
result=leap_frog(l,0)
if result== math.inf: 
    print(-1)
else:
    print(leap_frog(l,0))
