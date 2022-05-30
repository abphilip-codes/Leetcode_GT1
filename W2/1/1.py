# 547
# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def __init__(self):
        self.paths = []
        self.graph = {}

    def make(self, graph):
        for z, y in enumerate(graph):
            self.graph[z] = y

    def get(self, start, end, path):
        if(start==end):
            self.paths.append(path)
            return

        for z in self.graph[start]:
            self.get(z, end, path + [z])
            
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:           
        self.make(graph)
        self.get(0, len(graph)-1, [0])
        return self.paths