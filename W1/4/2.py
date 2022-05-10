# 417
# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        def dfs(z, y):
            if(z<0 or y<0 or z==m or y==n or grid2[z][y]==0): return True
            k = True
            if(grid1[z][y]==0): k = False
            grid2[z][y] = 0
            k = dfs(z+1, y) and k
            k = dfs(z-1, y) and k
            k = dfs(z, y+1) and k
            k = dfs(z, y-1) and k
            return k
        return sum(grid2[z][y] and dfs(z, y) for z in range(m) for y in range(n))