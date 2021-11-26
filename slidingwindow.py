def slidingWindow(s, t):
    
    need = {}
    window = {}
    
    for c in s:
        need[c] = need.get(c, 0) + 1
    
    left, right, valid, n = 0, 0, 0, len(s)
    
    while right < n:
        
        c = s[right]
        
        right += 1
        
        # do something in the window 
        
        print(f"window: {left} and {right}")
        
        
        while condition:
            
            d = s[left]
            
            left += 1
            
            # do something in the window 
    
    
        
        