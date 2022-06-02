# 1306
# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        b = collections.defaultdict(set)
        r = collections.defaultdict(set)
        for z in redEdges:
            u, v = z
            r[u].add(v)
        for z in blueEdges:
            u, v = z
            b[u].add(v)
        RED  = 0
        BLUE = 1 
        q = collections.deque()
        q.append((0, RED, 0))
        q.append((0, BLUE, 0))
        ans = dict(zip(range(n),[-1]*n))
        visited = set()
        visited.add((0, RED))
        visited.add((0, BLUE))
        
        while(q):
            node, par_edge, length = q.popleft()
            if(ans[node]==-1): ans[node] = length
            else: ans[node] = min(ans[node], length)
            
            if(par_edge == RED):
                if(node in b):
                    for child in b[node]:
                        if((child, BLUE) not in visited):
                            visited.add((child, BLUE))
                            q.append((child, BLUE, length + 1))
            elif(node in r):
                for child in r[node]:
                    if((child, RED) not in visited):
                        visited.add((child, RED))
                        q.append((child, RED, length + 1))
        
        return [ans[x] for x in range(n)]