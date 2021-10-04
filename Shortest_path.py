import heapq
from collections import defaultdict
from collections import deque
from math import dist, inf

edges = [[2,1,1],[2,3,1],[3,4,1]]

def convert(edges):
    ADlist = defaultdict(list)
    for edge in edges:
        ADlist[edge[0] - 1].append((edge[2], edge[1] - 1))

def Dijkstra(Edges, vi):
    
    n = len(Edges)  # assuming that the Edges is an adjacency list  (weight, vertex)
    heap = []
    heapq.heappush(heap, (0, vi))
    parent = list(range(n))
    seen = set()
    seen.add(vi)
    distance = [float(inf)]*n
    distance[vi] = 0
    
    while len(seen) != n:  
        w, node = heapq.heappop(heap)
        seen.add(node)
        for weight, neighbor in Edges[node]:
            if neighbor not in seen:
                # D[k][u] = min(D[k][u], D[k-1][v] + W(v, u))
                if w + weight < distance[neighbor]:
                    distance[neighbor] = w + weight
                    parent[neighbor] = node
                    heapq.heappush(heap, (w + weight, neighbor))
    return distance

def OriginalBellmanFord(edges, vi, n):                      # edge list
    dist = [float(inf) for i in range(n)]
    predecessor = [i for i in range(n)]
    dist[vi] = 0                             # be careful here, the vi is indexed from 0

    # the algorithm can be improved to loop at most n - 1 times by comparing old and new distance in each iteration, if it's 0, then break
    for _ in range(n - 1): 
        tmp = [float(inf)]*n
        tmp[vi] = 0
        for weight, source, target in edges:
            if weight + dist[source] < tmp[target]:
                tmp[target] = weight + dist[source]
                predecessor[target] = source
        dist[:] = tmp
    # to detect negative cycle, do one more iteration, if any distance decrease, then the negative cycle exist
    return dist, predecessor



def ImporvedBellmanFord(edges, vi, n):                      # edge list
    dist = [float(inf) for i in range(n)]
    predecessor = [i for i in range(n)]
    dist[vi] = 0                             # be careful here, the vi is indexed from 0

    # the algorithm can be improved to loop at most n - 1 times by comparing old and new distance in each iteration, if it's 0, then break
    for _ in range(n - 1):    
        flag = False # to exist the loop early
        for weight, source, target in edges:
            if weight + dist[source] < dist[target]:
                flag = True
                dist[target] = weight + dist[source]
                predecessor[target] = source
        if not flag:
            break
    # to detect negative cycle, do one more iteration, if any distance decrease, then the negative cycle exist
    return dist, predecessor
        


def SPFA(edges, vi, n):
    "shortest path faster algorithm"
    # here, we need to convert the edge list into adjacency list
    dist = [float(inf)]*n
    predecessor = [i for i in range(n)]
    dist[vi] = 0
    queue = deque()
    queue.append(vi)
    
    while queue:
        current = queue.popleft()
        for weight, neighbor in edges[current]:
            if weight + dist[current] < dist[neighbor]:
                predecessor[neighbor] = current
                dist[neighbor] = weight + dist[current]
                if neighbor not in queue: # here, the operation is O(v), which will increase the time complexity, so we might need to use set instead
                    queue.append(neighbor)
    
    return dist, predecessor


def FloydWarshall(edges, n):
    "here we need to convert the edge into adjacency matrix  O(n^3) complexity"
    
    dist = [[float(inf)]*n]*n
    Successor = [[None]*n]*n
    
    for u, v, w in edges:
        dist[u][v] = w
        Successor[u][v] = v
        
    for i in range(n):
        dist[i][i] = 0
        Successor[v][v] = v

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    Successor[i][j] = Successor[i][k]
    
    return dist, Successor

def PrintPath(Successor, u, v):
    if Successor[u][v] == None:
        return []
    
    start, end = u, v
    path = []
    while start != end:
        start = Successor[start][end]
        path.append(Successor[start][end])
    return path
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    
    
    
    

    
    
    
    