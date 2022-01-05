class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        """
        nlog(n)
        """
        
        dates = []
        for date in logs:
            dates.append((date[0], 1))
            dates.append((date[1], -1))
        
        dates.sort() # dominates
        
        ans, maxpop, cnt = 0, -float('inf'), 0
        
        for date, val in dates:
            
            cnt += val
            
            if cnt > maxpop:
                ans = date
                maxpop = cnt
        
        return ans
            

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        "O(n)"

        
        population = [0]*1001
        
        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1
            
        ans, maxpop, cnt = 0, -float('inf'), 0
        
        for i, val in enumerate(population):
            cnt += val
            if cnt > maxpop:
                ans = i + 1950
                maxpop = cnt
        
        return ans