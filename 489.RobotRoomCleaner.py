# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# backtracking
# when all of the direction for each cell has been explored, then stop

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def backtrack(coor, direc):
            seen.add(coor)
            robot.clean()
            
            for i in range(4):
                newd = (direc + i) % 4
                newcoor = (coor[0] + move[newd][0], coor[1] + move[newd][1])
                if newcoor not in seen and robot.move():
                    backtrack(newcoor, newd)
                    goback()
                robot.turnRight()
            
        # left right up down 
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        backtrack((0,0), 0)
        return 
        