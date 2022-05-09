# 1905
# https://leetcode.com/problems/count-sub-islands/

class Solution:    
    def help(self, grid, z, y, m, n):
            if(z<0 or z>=m or y<0 or y>=n): return
            if(grid[z][y]=="1"): grid[z][y] = "2" 
            else: return
            self.help(grid, z+1, y, m, n)
            self.help(grid, z-1, y, m, n)
            self.help(grid, z, y+1, m, n)
            self.help(grid, z, y-1, m, n)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for z in range(m):
            for y in range(n):
                if(grid[z][y]=="1"):
                    ans+=1
                    self.help(grid, z, y, m, n)
        return ans