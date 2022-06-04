# 1557
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(list(range(n))) - set([z[1] for z in edges]))