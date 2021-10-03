class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius
    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
            if x**2 + y**2 <= 1:
                return [x*self.r+self.x, y*self.r+self.y]
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius
    def randPoint(self) -> List[float]:
        r = self.r*math.sqrt(random.uniform(0,1))
        theta = random.uniform(0,1)*2*math.pi
        return [self.x + r*math.cos(theta), self.y + r*math.sin(theta)]