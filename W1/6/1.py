# 934
# https://leetcode.com/problems/shortest-bridge/

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        r, c = 0, 0
        for z in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[z][y] == 1:
                    r, c = z, y
                    break
        self.f1(grid, r, c, q)
        return self.f2(grid, q)
                 
    def f1(self, grid: List[List[int]], r: int, c: int, q: deque) -> None:
        m, n = len(grid), len(grid[0])
        grid[r][c] = 2
        s = [(r, c)]
        while(s):
            r, c = s.pop()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dr = r + dr
                dc = c + dc
                if (0<=dr<m and 0<=dc<n):
                    k = grid[dr][dc]
                    grid[dr][dc] = 2
                    if(k==2): continue
                    elif(k==0): q.append((dr, dc, 0))
                    else: s.append((dr, dc))
                        
    def f2(self, grid: List[List[int]], q: deque) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        while(q):
            for z in range(len(q)):
                r, c, t = q.popleft()
                if(t==1): return ans
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dr = r + dr
                    dc = c + dc
                    if(0<=dr<m and 0<=dc<n and grid[dr][dc]!=2):
                        q.append((dr, dc, grid[dr][dc]))
                        grid[dr][dc] = 2
            ans += 1
        return ans