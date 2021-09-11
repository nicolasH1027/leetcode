# #         DFS

# def DFS(node, target, visited):
    
#     # for the problem of exploring the graph
#     # the following line could be empyt
#     if node == target: return True
#     visited[node] = 1
#     for neighbor in node:
#         if neighbor not in visited:
#             visited[node] = 1
#             if DFS(neighbor, target, visited) == True:
#                 return True
        
#     return False
    

# def DFS(node, visited):
#     visited[node] = 1
#     for neighbor in node:
#         if neighbor not in visited:
#             visited[neighbor] = 1
#             DFS(neighbor,  visited)
            

# def DFSTraverse(G):
    
#     visited = [[False]]
#     count = 0
    
#     for node in G:
#         if node not in visited:
#             count += 1
#             DFS(node, visited)


# # DFS by stack
# root = 0
# stack = [root]
# visited = {root}

# while stack:
    
#     cur = stack.pop()
#     # return True if cur == target
#     for node in cur:
#         if node not in visited:
#             visited[node] = 1
#             stack.append(node)
            
    
# #       BFS
# def BFS(node, target, visited):
    
#     if node == target: return True
#     visited[node] = 1
    
#     for neighbor in node:
#         if neighbor not in visited:
#             visited[neighbor] = 1
#             if BFS(neighbor, target, visited) == True:
#                 return True 
        
#     return False


# def BFS(node, visited):
    
#     visited[node] = 1
    
#     for neighbor in node:
#         if neighbor not in visited:
#             visited[neighbor] = 1
#             BFS(neighbor, visited)
            
# def BFSTrverse(G):
    
#     visited = [[False]]
    
#     count = 0
    
#     for node in G:
#         if node not in visited:
#             count += 1
#             BFS(node, visited)
    
#     return count
    
# target = None
# root = 0
# visited = [root]
# from collections import deque

# queue = deque()
# queue.append(root)    
 
# while queue:
    
#     cur = queue.popleft()
#     if cur == target: return True
    
#     for node in cur:
#         if node not in visited:
#             visited.append(node)
#             queue.append(node)

       
    
    
    
    
    