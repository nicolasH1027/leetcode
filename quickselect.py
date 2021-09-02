
# only works for data without repeated value 
# for repated value, use the hash table firstly
import random

def quickselect(data, p, r, k):
    if p == r:
        return data[p]
    pivot = random.randrange(p,r+1)
    tmp = partition(data, p, r, pivot)
    
    if tmp == len(data) - k: return data[tmp]
    elif tmp < k:
        return  quickselect(data, tmp+1, r, k)
    else:
        return quickselect(data, p, tmp-1, k)
        
    

def partition(data, p, r, pivot):
    
    data[r], data[pivot] = data[pivot], data[r]
    x = data[r]
    i = p - 1
    for j in range(p, r):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    
    data[i+1], data[r] = data[r], data[i+1]
    return i+1  