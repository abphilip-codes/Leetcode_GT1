# 417
# https://leetcode.com/problems/a-b-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(z, y, k, h):
            if not (0<=z<R and 0<=y<C and heights[z][y]>=h and (z,y) not in k): return
            k.add((z,y))
            for r,c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(z+r, y+c, k, heights[z][y])
            
        R, C = len(heights), len(heights[0])
        a, b = set(), set()
        for z in range(C):
            dfs(0, z, a, -1)
            dfs(R-1, z, b, -1)
        for z in range(R):
            dfs(z, 0, a, -1)
            dfs(z, C-1, b, -1)       
        return a & b