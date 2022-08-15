import math
arr = []
counter = []
cont = []
for i in range(10):
    cont.append(0)
for x in range(0,10):
    counter.append(x)
nm = [8, 8, 5,6,3,1,5,9,7]
m = max(nm)
exp = 10
for x in nm:
    temp = x/exp
    value,second_value = math.modf(temp)
    val = value * exp
    arr.append(int(val))
for number in arr:
    if number == counter[number]:
        cont[number] += 1 
for contar in range(1,len(cont)):
    cont[contar] = cont[contar] + cont[contar-1]

    
print('arr:'+ str(arr))
print('cont:'+ str(cont))
    
    