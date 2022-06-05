# 1615 
# https://leetcode.com/problems/maximal-network-rank/

cclass Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        c2cs = defaultdict(set)
        for r in roads:
            c2cs[r[0]].add(r[1])
            c2cs[r[1]].add(r[0])
        h = list()
        for c, conns in c2cs.items():
            heapq.heappush(h, (-len(conns), c, tuple(conns)))
        firstcity = heapq.heappop(h)
        secondcity = heapq.heappop(h)
        firstrank = firstcity[0]
        secondrank = secondcity[0]
        cs_to_compare = [firstcity, secondcity]
        while h and h[0][0] == secondrank:
            cs_to_compare.append(heapq.heappop(h))
        #print(cs_to_compare)
        for i in range(len(cs_to_compare)-1):
            for j in range(i+1, len(cs_to_compare)):
                c1 = cs_to_compare[i]
                c2 = cs_to_compare[j]
                is_connected = c1[1] in c2[2]
                nr = -c1[0] + (-c2[0]) - is_connected
                if nr == -firstrank + -secondrank: return nr
        return -firstrank + -secondrank - 1