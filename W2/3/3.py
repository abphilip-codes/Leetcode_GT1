# 847
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        self.count = 0
        for edge in connections:
            self.graph[edge[0]].append(edge[1])
        self.visited = [0]*n
        for z in range(n):
            if not self.visited[z]: self.f(z)
        return self.count
    
    
    def f(self, start):
        found = False
        neighbors = self.graph[start]
        self.visited[start] = 1
        for neighbor in neighbors:
            if not neighbor: found = True
            if not self.visited[neighbor]:
                found = self.f(neighbor)
                if not found: self.count += 1
        return found