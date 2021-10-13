class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        seen = set()
        stack = [0]
            
        while stack:
            key = stack.pop()
            if key in seen: continue
            seen.add(key)
            for room in rooms[key]:
                stack.append(room)
        return len(seen) == len(rooms)