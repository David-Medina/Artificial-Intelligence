linus = {}
def recursive_stairs(stair,step):
    if step >= len(stair):
        return stair[-1]
    else:
        if step not in linus:
            linus[step]=min(recursive_stairs(stair,step+1),recursive_stairs(stair,step+2))+stair[step]
    return linus[step]

n = int(input())
valor = input().split(" ")

l=[]
for i in valor:
    l.append(int(i))

print(min(recursive_stairs(l,0),recursive_stairs(l,1)))

    
    
            
        
    
    
    