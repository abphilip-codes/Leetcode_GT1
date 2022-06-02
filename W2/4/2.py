# 1654
# https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.count = 0
        dep, arr = {}, {}
        for x,y in connections:
            for a,b,d in [[x,y,dep],[y,x,arr]]:
                if not a in d: d[a] = [b]
                else: d[a].append(b)
        visited = set()

        def f(x):
            if(x in visited): return
            visited.add(x)
            if(x in arr):
                for y in arr[x]: f(y)
            if(x in dep):
                for y in dep[x]:
                    if not y in visited:
                        self.count+=1
                        f(y)
        f(0)
        return self.count