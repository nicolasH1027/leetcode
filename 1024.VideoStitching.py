class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        clips.sort(key = lambda x: (x[0], -x[1]))
        
        cnt, i, curEnd, nextEnd = 0, 0, 0, 0
        
        while i < len(clips) and clips[i][0] <= curEnd:
            
            cnt += 1
            
            while i < len(clips) and clips[i][0] <= curEnd:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1
            
            curEnd = nextEnd
            
            if nextEnd >= time:
                return cnt
        
        return -1