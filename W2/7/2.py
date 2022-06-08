# 886 
# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        e = [[] for _ in range(n+1)]
        for d in dislikes:
            e[d[0]].append(d[1]) 
            e[d[1]].append(d[0])
        
        c = [0]*(n+1)
        for p in range(1, n+1):
            if c[p]: continue
            
            s, c[p] = [p], 1
            while(s):
                p = s.pop()
                for z in e[p]:
                    if(c[z]==c[p]): return False
                    if not c[z]:
                        c[z] = 1 if(c[p]==2) else 2
                        s.append(z)
        return True