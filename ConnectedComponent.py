"""
求graph 中各个强连通分量
"""

"""
无向图

在无向图中，连通分量就是强连通分量， 只需要对每一个node进行dfs，同时用
visited 记录访问过的节点，就可以找出所有联通分量了.
"""
seen = set()
graph = collections.defaultdict(list)
def dfs(root):
    
    for nxt in graph[root]:
        if nxt not in seen:
            seen.add(nxt)
            dfs(nxt)

"""
有向图

在有向图中， 强连通分量指的是， 分量中任意两点间都有路径彼此相连，
注意的是，因为是有向图，所以，既要有 i -> j， 也需要 j -> i。

有如下三个可以用于在线性时间内寻找一个有向图中的强连通分量的算法
Kosaraju algorithm
Tarjan algorithm
Gabow algorithm, very similar with Tarjan algorithm, no need to know about it
"""


"""
图的转置， 既将有向图中所有边的方向转置 从 i -> j 改成 j -> i
"""

"""
Kosaraju algorithm

1. 将图转置
2. dfs 以逆后序的顺序遍历转置后的图 并将遍历结果保存
3. dfs 以保存的逆后序的结果遍历原图。 具体证明请参考算法导论第三版615页
"""

"https://www.zhihu.com/question/58926821"
"https://www.cnblogs.com/nullzx/p/6437926.html"
"https://redspider110.github.io/2018/08/22/0092-algorithms-topological-sorting/"
"https://www.programiz.com/dsa/strongly-connected-components"

"和拓扑排序非常类似， 具体理解可能得参考上述几个链接"

graph = collections.defaultdict(list) # hold the edge list
vertes = [] # hold all the vertex in graph

def invergraph(graph):
    "1.图转置"
    Invert_Graph = collections.defaultdict(list)
    
    for src in graph:
        for tar in graph[src]:
            Invert_Graph[tar].append(src)
            
    return Invert_Graph

def find_order(vertes):
    "2.求逆后序"
    seen = set()
    order = []
    for src in vertes:
        if src in seen: continue
        seen.add(src)
        reverse_postorder(src, order)
    return order

def reverse_postorder(root, order):
    for tar in graph[root]:
        if tar in seen: continue
        seen.add(tar)
        reverse_postorder(tar, order)
    order.append(root)

def dfs(root):
    ans = [root]
    for tar in graph[root]:
        if tar in seen: continue
        seen.add(tar)
        ans.extend(dfs(tar))
    return ans
    
def Find_SCC(order):
    "3. 以 逆后序 的顺序 先序遍历原图， 没有语病"
    seen = set()
    ans = []
    for src in order:
        if src in seen: continue
        seen.add(ans)
        ans.append(dfs(src))
    return ans


"""
Tarjan algorithm

Tarjan algorithm 不需要计算图的转置，并且只需要遍历图一次

多了 ind = [] 和 low = [] 两个数组， ind 用于记录dfs的访问顺序，
low 用于记录栈内能够访问到的最小顺序
其实这个low记载的数值呢， 用二叉树来理解的话，就是最小公共爹的概念。
(lowest common ancestor)，就是最大强连通分量里，各点能够到达的
有着最小访问顺序的那个node。

0 -- 3
|    |
1 -- 2

假设从 0 开始， 0 -> 1 -> 2 -> 3 -> 0
那么， 1能到达的最早访问点是什么，是 0
同理， 2呢？ 也是0
同理， 3呢？ 也是0
"""

"https://www.youtube.com/watch?v=TyWtx7q2D7Y&ab_channel=WilliamFiset"

class Tarjan:
    
    def __init__(self, n) -> None:
        self.graph = collections.defaultdict(list)
        self.prev = 1
        self.num = n
        self.count = 0
  
    def add(self, u, v):
        self.graph[u].append(v)

    def TarjanSCC(self):
        """
        idx 数组用于记录每个node被访问的时间顺序
        low 根据前文解释，用于记录最大联通分量里的最小公共爹
        stack 用于确定是否回到最大联通分量里的最小公共爹
        onstack 这个比较难理解，用于确定遇到的点是否属于同一个
        联通分量，并以此进行更新
        """
        n = self.num
        self.idx, self.low= [0]*n, [0]*n
        self.stack, self.onstack = [], set()
        
        for node in range(n):
            if not self.idx[node]:
                "如果node没被访问过, 则递归调用dfs"
                self.dfs(node)
        
        "最后返回low数组，相同的值代表同一个联通分量"
        return self.low, self.count
    
    def dfs(self, node):
        """
        prev 记录访问顺序，从1开始
        """
        self.idx[node] = self.low[node] = self.prev
        self.stack.append(node)
        self.onstack.add(node)
        self.prev += 1
        
        for nxt in self.graph[node]:
            "对于node的邻居节点，如果没有访问过，则调用递归"
            if not self.idx[nxt]:
                self.dfs(nxt)
            """
            运行到此处，说明遇到已经访问过的节点，那么，如果它在onstack，那么
            说明nxt点与node点属于同一个联通分量，那么更新node的最小公共爹
            """
            if nxt in self.onstack:
                self.low[node] = min(self.low[node], self.low[nxt])
            
        """
        运行到此处，说明已经到达某个联通分量的最小公共爹，也意味着我们已经把此最小
        公共爹对应的强联通分量中的点压入栈中，那么我们需要把他们pop出来，而且把对应
        onstack中的node清理出去
        """
        if self.low[node] == self.idx[node]:
            
            while True:
                cur = self.stack.pop()
                self.onstack.remove(cur)
                # self.low[cur] = self.idx[node]
                if cur == node:
                    break
            self.count += 1