# 1319
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.c = 0
        self.p = [-1 for _ in range(n)]        
        for n1, n2 in connections: self.u(n1,n2)        
        s = -1
        for z in self.p:
            if(z<0): s+=1                
        if(s<=self.c): return(s)        
        return -1
    
    def u(self, n1, n2):
        p1, p2 = self.f(n1,n2)        
        if(p1!=p2):            
            if(self.p[p1] < self.p[p2]):               
                self.p[p1] += self.p[p2]
                self.p[n2] = p1
                self.p[p2] = p1
            else:
                self.p[p2] += self.p[p1]
                self.p[n1] = p2
                self.p[p1] = p2
        else: self.c += 1        
        
    def f(self, n1, n2):
        p1 = n1
        p2 = n2        
        while(self.p[p1]>=0):
            p1 = self.p[n1]
            n1 = p1  
        while(self.p[p2]>=0):
            p2 = self.p[n2]
            n2 = p2
        return (p1,p2)