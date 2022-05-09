# 695
# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        a, b = len(grid), len(grid[0])
        s, ans, k = set(), 0, 0
        for z in range(a):
            for y in range(b):
                arr, k = [(z,y)], 0
                while(arr):
                    r, c = arr[-1]
                    arr.pop(-1)
                    if r<0 or r>=a or c<0 or c>=b or (r, c) in s or grid[r][c]!=1:
                        continue
                    k+=1
                    s.add((r, c))
                    arr.append((r-1, c))
                    arr.append((r+1, c))
                    arr.append((r, c-1))
                    arr.append((r, c+1))
                ans = max(ans, k)
        return ans