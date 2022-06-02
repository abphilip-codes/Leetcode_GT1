# 365
# https://leetcode.com/problems/water-and-jug-problem/

import math
class Solution:
    def canMeasureWater(self, a: int, b: int, c: int) -> bool:
        return False if(a+b<c) else True if(a+b==0) else not (c%math.gcd(a, b))