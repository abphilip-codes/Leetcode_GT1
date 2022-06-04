# 997
# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        ans = self.f(start, end, bank, [])
        if(ans==float('inf')): return -1
        else: return ans    
            
    def d(self, s1, s2, c=0):
        for z in range(len(s1)):
            if s1[z]!=s2[z]: c+=1
            if c>1: return False
        return c==1
       
    def f(self, start, end, bank, path):
        if self.d(start, end): return 1
        else:
            k = float('inf')
            for z in bank:
                if(z!=end and self.d(start, z) and z not in path):
                    k = min(1+self.f(z, end, bank, path+[z]), k)
            return k