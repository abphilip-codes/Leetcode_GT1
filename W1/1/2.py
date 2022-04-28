# 200
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        k, ans = set(), 0
        def bfs(z,y):
            if(z<0 or y<0 or z==r or y==c or 
              (z,y) in k or grid[z][y]=="0"): return 
            k.add((z,y))
            for a,b in [[1,0],[-1,0],[0,1],[0,-1]]: bfs(z+a,y+b)
                
        for z in range(r):
            for y in range(c):
                if(grid[z][y]=="1" and (z,y) not in k):
                    bfs(z,y)
                    ans+=1
        return ans