# 1926
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        d = ((0,1), (0,-1), (1,0), (-1,0))
        
        q = deque([(entrance[0], entrance[1])])
        k, p = set([(entrance[0], entrance[1])]), 0
        
        while(q):
            for z in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d: 
                    dr, dc = dr + r, dc + c
                    if not (0<=dr<m and 0<=dc<n):
                        if((r, c)!=(entrance[0], entrance[1])): return p
                        continue
                        
                    if((dr, dc) not in k and maze[dr][dc]=="."):
                        k.add((dr, dc))
                        q.append((dr, dc))
            p+=1        
        return -1