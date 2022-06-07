# 785 
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def f(s, k):
            k[s], q = 1, []
            q.append(s)
            while(q):
                top = q.pop()
                for z in graph[top]:
                    if(k[z]==-1):
                        k[z]=1-k[top]
                        q.append(z)
                    elif(k[z]==k[top]): return False
            return True
        n = len(graph)
        k = [-1]*n
        for z in range(n):
            if(k[z]==-1):
                if not f(z, k): return False
        return True