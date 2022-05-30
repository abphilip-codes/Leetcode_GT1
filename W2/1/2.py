# 1319
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from collections import defaultdict
class Solution:    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def make(self, rooms):
        for z, y in enumerate(rooms): self.graph[z] = y
            
    def get(self, rooms, room):
        if not self.visited[room]:
            self.visited[room] = True
            for y in self.graph[room]: self.get(rooms, y)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False] * len(rooms) 
        self.make(rooms)
        self.get(rooms, 0)
        return all(self.visited)