# 547
# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = len(isConnected)
        n, a, b = 0, set(), set(range(d))
        while(b):
            n+=1
            a.add(b.pop())
            while(a):
                z = a.pop()
                for y, t in enumerate(isConnected[z]):
                    if t and y in b:
                        a.add(y)
                        b.remove(y)
        return n