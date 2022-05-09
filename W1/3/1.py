# 1020
# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        k, q = set(), [(sr, sc)]
        o = image[sr][sc]
        while(q):
            z, y = q.pop(0)
            k.add((z,y))
            image[z][y] = newColor
            for x, w in [(1,0), (0, 1), (-1, 0), (0,-1)]:
                if(z+x in range(0,len(image)) and y+w in range(0,len(image[0]))):
                    if(image[z+x][y+w]==o and (z+x,y+w) not in k): q.append((z+x, y+w))
        return image 