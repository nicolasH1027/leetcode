# O(n) solution with quick select. The question ganrautee that there is no repeated value

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ind = self.quickselect(points, 0, len(points) - 1, k)
        return points[:ind+1]
        
            
    def dist(self, item):
        return math.sqrt(item[0]**2 + item[1]**2) 

    def quickselect(self, data, p, r, k):
        if p == r:
            return p
        pivot = random.randint(p,r)
        tmp = self.partition(data, p, r, pivot)

        if tmp == k - 1: return tmp
        elif tmp < k:
            return  self.quickselect(data, tmp+1, r, k)
        else:
            return self.quickselect(data, p, tmp-1, k)



    def partition(self, data, p, r, pivot):

        data[r], data[pivot] = data[pivot], data[r]
        x = self.dist(data[r])
        i = p - 1
        for j in range(p, r):
            if self.dist(data[j]) <= x:
                i = i + 1
                data[i], data[j] = data[j], data[i]

        data[i+1], data[r] = data[r], data[i+1]
        return i+1  