# 433
# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = []
        q.append([start, arr[start]])
        visited = set()
        visited.add(start)
        while len(q) > 0:
            l, v = q.pop(0)
            if(v==0): return True
            if(l-v>=0 and (l-v) not in visited):
                q.append([l-v, arr[l-v]])
                visited.add(l-v)               
            if(l+v<len(arr) and (l+v) not in visited):
                q.append([l+v, arr[l+v]])
                visited.add(l+v) 
        return False