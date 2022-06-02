# 1654
# https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if not x: return 0
        
        threshold = max(forbidden+[x]) + a+b
        forbidden = set(forbidden)
        seen = set([0])
        q = [[0,0]]
        
        while(q):
            pos, steps = q.pop(0)
            if(pos+a not in forbidden and pos+a not in seen and pos+a<=threshold):
                if(pos+a==x): return steps+1
                q.append([pos+a, steps+1])
                seen.add(pos+a)
                
            if(pos-b>0 and pos-b not in forbidden and pos-b not in seen): 
                if(pos-b==x): return steps+1
                seen.add(pos-b)
                
                if(pos-b+a not in forbidden and pos-b+a not in seen and pos-b+a<=threshold):
                    if(pos-b+a==x): return steps+2
                    q.append([pos-b+a, steps+2])
                    seen.add(pos-b+a)
        return -1