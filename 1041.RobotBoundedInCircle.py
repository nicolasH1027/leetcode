class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        idx = 0
        
        x = y = 0
        
        for i in instructions:
            
            if i == 'L':
                idx = (idx + 3) % 4
            
            elif i == 'R':
                idx = (idx + 1) % 4
            
            else:
                x += direc[idx][0]
                y += direc[idx][1]
        
        return (x == 0 and y == 0) or idx != 0