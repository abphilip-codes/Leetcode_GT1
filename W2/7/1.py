# 1615 
# https://leetcode.com/problems/maximal-network-rank/

cclass Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        c = defaultdict(set)
        for r in roads:
            c[r[0]].add(r[1])
            c[r[1]].add(r[0])
        h = []
        for k1, k2 in c.items():
            heapq.heappush(h, (-len(k2), k1, tuple(k2)))
        a1 = heapq.heappop(h)
        a2 = heapq.heappop(h)
        b1 = a1[0]
        b2 = a2[0]
        p = [a1, a2]
        while(h and h[0][0]==b2):
            p.append(heapq.heappop(h))
        for z in range(len(p)-1):
            for y in range(z+1, len(p)):
                c1, c2 = p[z], p[y]
                l = c1[1] in c2[2]
                d = -c1[0] + (-c2[0]) - l
                if(d==-b1+-b2): return d
        return -b1+-b2-1