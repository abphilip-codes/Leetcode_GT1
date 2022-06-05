# 886
# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        enemies = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            enemies[dislike[0]].append(dislike[1]) 
            enemies[dislike[1]].append(dislike[0])
        
        colors = [0] * (n + 1)
        for person in range(1, n + 1):
            if colors[person]:
                continue
            
            stack = [person]
            colors[person] = 1
            while stack:
                p = stack.pop()
                for enemy in enemies[p]:
                    if colors[enemy] == colors[p]:
                        return False
                    if not colors[enemy]:
                        colors[enemy] = 1 if colors[p] == 2 else 2
                        stack.append(enemy)
        return True