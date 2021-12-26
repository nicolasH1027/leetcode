
# only works for data without repeated value 
# for repated value, use the hash table firstly
import random
"""
return the starting index of top K element
"""
def quickselect(data, l, r, k):
    if l == r:
        return l
    pivot = random.randint(l,r)
    tmp = partition(data, l, r, pivot)
    
    if tmp == len(data) - k: return tmp
    elif tmp < len(data) - k:
        return  quickselect(data, tmp+1, r, k)
    else:
        return quickselect(data, l, tmp-1, k)
        
    

def partition(data, l, r, pivot):
    
    data[r], data[pivot] = data[pivot], data[r]
    x = data[r]
    i = l - 1
    for j in range(l, r):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    
    data[i+1], data[r] = data[r], data[i+1]
    return i+1 

"""
return the ending index of lower K element
"""
def quickselect(data, l, r, k):
    if l == r:
        return l
    
    pv = random.randint(l, r)
    tmp = partition(data, l, r, pv)
    if tmp == k - 1: return tmp
    if tmp > k - 1:
        return quickselect(data, l, tmp - 1, k)
    else:
        return quickselect(data, tmp + 1, r, k)
    

def partition(data, l, r, pivot):
    
    data[pivot], data[r] = data[r], data[pivot]
    x, j = data[r], l-1
    
    for i in range(l, r):
        if data[i] <= x:
            j += 1
            data[j], data[i] = data[i], data[j]
    data[j+1], data[r] = data[r], data[j+1]
    
    return j + 1
    
            
    
    
    
    