class heapqueue:
    
    def __init__(self, ls = []) -> None:
        self.data = ls
    
    
    def heappush(self, val):
        
        self.data.append(val)
        if len(self.data) == 1:
            return None
        self.upAdjust()
        
    def upAdjust(self):
        
        child_index = len(self.data) - 1
        parent_index = child_index // 2
        tmp = self.data[child_index]
        
        while child_index > 0 and tmp < self.data[parent_index]:
             
             self.data[child_index] = self.data[parent_index]
             child_index = parent_index
             parent_index //= 2
             
        self.data[child_index] = tmp
    
    def heappop(self):
        
        if len(self.data) == 0:
            print("no element in the heap")
            return None
        
        if len(self.data) == 1:
            return self.data.pop()
        
        head = self.data[0]
        self.data[0] = self.data.pop()
        self.downAdjuct()
        
        return head
    
    def downAdjust(self, parent = 0):
        
        # parent = 0
        tmp = self.data[parent]
        childIndex = 2*parent + 1
        
        while childIndex  < len(self.data):
            
            if childIndex + 1 < len(self.data) and self.data[childIndex + 1] < self.data[childIndex]:
                childIndex += 1
                
            if tmp <= self.data[childIndex]:
                break
            
            self.data[parent] = self.data[childIndex]
            parent = childIndex
            childIndex = 2*childIndex + 1
        
        self.data[parent] = tmp
    
    def heapify(self, ls):
        
        self.data = ls
        nonleafnode = len(ls)//2 - 1 # index
        for i in range(nonleafnode, -1, -1):
            self.downAdjust(i)