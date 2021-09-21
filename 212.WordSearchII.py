class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        # we define our trie structure here
        # the end mark is used to track the potential answer, check later
        trie = {}
        end = 'end'
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[end] = end
        m = len(board)
        n = len(board[0])
        result = []
        
        
        def backtrack(row, col, node, track):
            # if end mark visted, then record the answer, and remove the end mark
            if end in node:
                result.append("".join(track[:]))
                node.pop(end)
            
            # out of bound case
            if row < 0 or row >= m or col < 0 or col >= n or (row, col) in seen:            
                return
            
            # not a valid answer
            if board[row][col] not in node:
                return
            
            # we use a hashset here to keep track of visited board cell
            
            seen.add((row, col))
            track.append(board[row][col])
            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                backtrack(row+i, col+j, node[board[row][col]], track)
            track.pop()
            seen.remove((row, col))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    seen = set()
                    backtrack(i, j, trie, [])
        return result