# 1162
# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q, n = deque(), len(grid)
        for z in range(n):
            for y in range(n):
                if(grid[z][y]):
                    q.append((z, y))
                    grid[z][y] = -1
        ans = -1
        while(q):
            x, w = q.popleft()
            for x1, w1 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x2, w2 = x + x1, w + w1
                if(0<=x2<n and 0<=w2<n and grid[x2][w2]==0):
                    grid[x2][w2] = grid[x][y] + 1 if grid[x][w] != -1 else grid[x][w] + 2
                    ans = max(ans, grid[x2][w2])
                    q.append((x2, w2))
        return ans