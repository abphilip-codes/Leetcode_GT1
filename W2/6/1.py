# 997
# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust: return 1 if(n==1) else -1
        p = set([z[0] for z in trust])
        t = (n*(n+1))/2
        j = t - sum(p)
        if(j):
            c = [z[0] for z in trust if(z[1]==j)]
            if(t-sum(c)==j): return int(j)
            else: return -1
        else: return -1