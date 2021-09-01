# quick sort 
# without randomization

def quicksort(data, p, r):
    if p < r:
        q = partition(data, p, r)
        quicksort(data, p, q - 1)
        quicksort(data, q + 1, r)

def partition(data, p, r):
    x = data[r]
    i = p - 1
    for j in range(p, r - 2):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    
    data[i+1], data[r] = data[r], data[i+1]
    return i+1    

# quick sort 
# with randomization

