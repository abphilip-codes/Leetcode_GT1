# 1254
# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        a, b = len(grid), len(grid[0])
        arr, ans = [[0, 1], [0, -1], [1, 0], [-1, 0]], 0
        def dfs(y, x, s):
            grid[y][x] = 1
            for k1, k2 in arr:
                n, m = y+k1, x+k2
                if(n>=a or n<0 or m>=b or m<0): s=0
                else:
                    if(grid[n][m] == 0 and not dfs(n, m, s)): s=0
            return s
        for z in range(a):
            for y in range(b):
                if(grid[z][y]==0): ans+=dfs(z, y, 1)
        return ans