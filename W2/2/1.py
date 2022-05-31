# 1376
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        k = [-1]*n
        for z in range(n):
            if(k[z]==-1):
                k[z], t = 0, 0
                while(z!=headID):
                    z = manager[z]
                    t += informTime[z]
                    if(t>k[z]): k[z] = t
                    else: break
        return k[headID]