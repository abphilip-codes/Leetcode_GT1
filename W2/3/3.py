# 847
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.extraConn = 0
        self.parent = [-1 for _ in range(n)]        
        for n1, n2 in connections:
            self.Union(n1,n2)        
        n_s = -1
        for p in self.parent:
            if p < 0:
                n_s += 1                
        if n_s <= self.extraConn:
            return(n_s)        
        return -1
    
    def Union(self, n1, n2):
        p1, p2 = self.Find(n1,n2)        
        
        if p1 != p2:            
            if self.parent[p1] < self.parent[p2]:               
                self.parent[p1] += self.parent[p2]
                self.parent[n2] = p1
                self.parent[p2] = p1
                
            else:
                self.parent[p2] += self.parent[p1]
                self.parent[n1] = p2
                self.parent[p1] = p2
                
        else:            
            self.extraConn += 1        
        
    def Find(self, n1, n2):
        p1 = n1
        p2 = n2        
        while self.parent[p1] >= 0:
            p1 = self.parent[n1]
            n1 = p1
            
        while self.parent[p2] >= 0:
            p2 = self.parent[n2]
            n2 = p2
            
        return (p1,p2)