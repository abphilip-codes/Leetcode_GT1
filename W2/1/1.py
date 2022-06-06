# 547
# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        k = list(range(len(isConnected)))
        while(k):
            s = [k.pop(0)]
            while(s):
                c = s.pop()
                for z in [z for z in k if isConnected[c][z]]:
                    k.remove(z)
                    s.append(z)
            ans+=1
        return ans