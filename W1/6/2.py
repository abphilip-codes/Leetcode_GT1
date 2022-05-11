# 1926
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = mat[:]
        for z in range(m):
            for y in range(n):
                if(mat[z][y]!=0):
                    if(z==0 and y==0): d[z][y] = 10000
                    elif(z==0): d[z][y] = mat[z][y-1] + 1
                    elif(y==0): d[z][y] = mat[z-1][y] + 1
                    else: d[z][y] = min(mat[z-1][y], mat[z][y-1]) + 1

        for z in range(m-1,-1,-1):
            for y in range(n-1, -1, -1):
                if(mat[z][y]!=0):
                    if(z==m-1 and y==n-1):
                        mat[z][y] = d[z][y]
                    elif(z==m-1):
                        mat[z][y] = min(d[z][y], 1+mat[z][y+1])
                    elif(y==n-1):
                        mat[z][y] = min(d[z][y], 1+mat[z+1][y])
                    else:
                        mat[z][y] = min(d[z][y], 1+min(mat[z+1][y], mat[z][y+1]))
        return mat