# 847
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

from math import inf
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodeCount = len(graph)
        masks = [1 << z for z in range(nodeCount)]
        allVisited = (1 << nodeCount) - 1
        queue = deque([(z, masks[z]) for z in range(nodeCount)])
        steps = 0
        visited_states = [{masks[z]} for z in range(nodeCount)]
        while(queue):
            count = len(queue)
            while(count):
                currentNode, visited = queue.popleft()
                if(visited == allVisited): return steps
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    if(new_visited==allVisited): return steps + 1
                    if(new_visited not in visited_states[nb]):
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))
                count-=1
            steps+=1
        return inf