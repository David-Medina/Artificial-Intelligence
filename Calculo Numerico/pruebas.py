
def two_sums(nums,target):
    for j in range(len(nums)):
        for i in range(1,len(nums)):
            if i is not j:
                if nums[i]+nums[j] == target:
                    res.append(j)
                    res.append(i)
                    return res  
        
            
           


res = []
n = [3,2,3]
t = 6
print(two_sums(n,t))