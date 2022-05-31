# 802
# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def f(k):
            d[k]=1
            for z in graph[k]:
                if(d[z]==0): f(z)
                if(d[z]==1): return 
            d[k]=2
            return 
        n = len(graph)
        d = [0]*n
        for z in range(n):
            if(d[z]==0): f(z)
        return [z for z in range(n) if d[z]==2 ] 