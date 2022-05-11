# 934
# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        a, b = len(grid), len(grid[0])
        if(grid[0][0]==1 or grid[-1][-1]): return -1
        k = [[False for z in range(b+1)] for j in range(a+1)]
        x1, y1 = [1,-1,0,0,-1,1,1,-1], [0,0,1,-1,-1,1,-1,1]
        q, k[0][0] = deque(), True
        q.append((0,0,0))
        while(q):
            x, y, d = q.popleft()
            if(x==a-1 and y==a-1): return d+1
            for z in range(8):
                r = x + x1[z]
                c = y + y1[z]
                if(r<0 or c<0 or r>a-1 or c>b-1 or k[r][c] or grid[r][c]): continue
                q.append((r,c,d+1))
                k[r][c] = True
        return -1