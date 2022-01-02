"""
注意， 一般来说，割点和桥是定义在无向图中的概念。 如果是有向图，可能需要问清楚具体怎么定义的。

割点， 如果移除这个node以及与其对应的edge，那么剩下的点构成的联通分量数量会增加。
桥， 如果移除这个edge， 那么剩下的点构成的联通分量会增加

割点与桥 两者间并不意味着彼此的存在

具体关系参考如下链接
https://my.oschina.net/u/4330588/blog/3841704
"""

"""
Tarjan algorithm

Tarjan 算法最重要的两个概念就是， idx访问时间数组以及
low最小公共爹数组。通过这个两组对应值得比较，我们可以得出
割点和桥，下面是具体解释。
"""

"""
割点

1 -> 2 -> 3 -> 1 -> 3 -> 4 -> 5

（1） 第一种情况
此时， 3既为割点。回忆上一篇关于最强联通分量的讲解，当时讲了一个最小
公共爹的概念，我们此时在这一问题中应用这个概念。对于 1 2 3， 此时他们的
最小公共爹是1（假设从1开始遍历），那么， 对于4 5， 如果他们的最小公共爹大于等于3，
此刻为 3， 那么意味着他们必须通过3 才能回到1，那么如果把3删去，就可以得到两个
不同的联通分量。

（2）第二种情况
假设最小公共爹是根节点（dfs遍历的根节点）， 那么，如果此根节点
有两个或者两个以上的子节点，那么把最小公共爹删掉，剩下的子树就自然而然分裂成若干
个联通分量。

注意，我们这里探讨的是无向图！
"""

class Tarjan:
    
    def __init__(self, nums) -> None:
        self.graph = collections.defaultdict(list)
        self.nums = nums
        self.step = 1
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def ArticuPoint(self):
        
        n = self.nums
        self.ans, self.idx, self.low = set, [0]*n, [0]*n
        
        """
        for loop 是为了解决出现若干个连通图的状况
        """
        for i in range(n):
            if not self.idx[i]:
                self.dfs(i, i)
        
        return self.ans
        
    def dfs(self, cur, parent):
        self.child = 0
        self.idx[cur] = self.low[cur] = self.step
        self.step += 1
        
        for nxt in self.graph[cur]:
            
            "如果未曾被访问过，那么进行递归调用"
            if not self.idx[nxt]:
                self.child += 1
                self.dfs(nxt, cur)
                self.low[cur] = min(self.low[cur], self.low[nxt])
                
                if cur != parent and self.low[nxt] >= self.idx[cur]:
                    self.ans.add(cur)

            # 如果已经被访问过，而且不是根节点，那么我们对此更新cur的low值
            elif cur != parent:
                self.low[cur] = min(self.low[cur], self.idx[nxt])
                    
        """
        判断根节点的情况
        """
        if cur == parent and self.child >= 2:
            self.ans.add(cur)
            

"""
割边

1 -> 2 -> 3 -> 1 -> 3 -> 4 -> 5

因为是割边，所以我们不需要探讨根节点的情况（为什么呢？）。第二个要改动的是，
以上面这个例子来说， 如果最小公共爹大于3， 那么意味着子节点无法不经过3，而
返回1，因此，此时 3 - 4， 4- 5就是割边
"""

class Tarjan:
    
    def __init__(self, nums) -> None:
        self.graph = collections.defaultdict(list)
        self.nums = nums
        self.step = 1
        self.count = 0
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def ArticuEdge(self):
        
        n = self.nums
        self.ans, self.idx, self.low = [], [0]*n, [0]*n
        for i in range(n):
            if not self.idx[i]:
                self.dfs(i, -1)
        
        return self.ans, self.count
        
    def dfs(self, cur, parent):
        
        self.idx[cur] = self.low[cur] = self.step
        self.step += 1
        
        for nxt in self.graph[cur]:
            
            "从爹而来，又到回爹，那么这条到回爹的路肯定不是桥"
            if nxt == parent: continue 
            
            if not self.idx[nxt]:
                self.dfs(nxt, cur)
                self.low[cur] = min(self.low[cur], self.low[nxt])
                
                """
                nxt 最小公共爹大于 cur 的访问顺序，说明nxt不能经过cur回到
                更早的点，因为nxt最早只能回到low[nxt]，所以，
                """
                if self.idx[cur] < self.low[nxt]:
                    self.ans.append([cur, nxt])
                    self.count += 1
            elif self.idx[nxt]:
                self.low[cur] = min(self.low[cur], self.idx[nxt])