class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        res = 0
        queue = collections.deque()
        
        for item in nestedList:
            queue.append((item, 1))
            
        while queue:
            cur, level = queue.popleft()
            if cur.isInteger():
                res += cur.getInteger() * level
            else:
                for item in cur.getList():
                    queue.append((item, level+1))
        
        return res
    
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        res = 0
        stack = []
        
        for item in nestedList:
            stack.append((item, 1))
            
        while stack:
            cur, level = stack.pop()
            if cur.isInteger():
                res += cur.getInteger() * level
            else:
                for item in cur.getList():
                    stack.append((item, level+1))
        
        return res

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def dfs(root, level):
            
            total = 0
            
            for item in root:
                if item.isInteger():
                    total += item.getInteger() * level
                else:
                    total += dfs(item.getList(), level + 1)

            return total
        return dfs(nestedList, 1)
            