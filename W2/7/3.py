# 785 
# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bipar(src,color):
            color[src]=1
            queue=[]
            queue.append(src)
            while (queue):
                top=queue.pop()
                for neigh in graph[top]:
                    if color[neigh]==-1:
                        color[neigh]=1-color[top]
                        queue.append(neigh)
                    elif color[neigh]==color[top]:
                        return False
            return True
        n=len(graph)
        color=[-1]*n
        for i in range(n):
            if color[i]==-1:
                if not bipar(i,color):
                    return False
        return True