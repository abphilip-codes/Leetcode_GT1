# 1020
# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        a, b = len(grid), len(grid[0])
        def dfs(z, y):
            if not (0<=z<a and 0<=y<b and grid[z][y]==1): return 0
            grid[z][y], ans = 0, 0
            for m, n in [(0,1),(1,0),(0,-1),(-1,0)]:
                ans+=dfs(z+m,y+n)
            return ans+1 
        for z in range(a):
            for y in range(b):
                if(z*y*(a-z-1)*(b-y-1)==0): dfs(z,y)
        return sum(sum(z) for z in grid)