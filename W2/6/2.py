# 1557
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if("0000" == target): return 0
        if("0000" in deadends or target in deadends): return -1
        v = {}
        v["0000"] = 0
        q = collections.deque()
        q.append("0000")
        
        vr = {}
        vr[target] = 0
        qr = collections.deque()
        qr.append(target)
        
        d = {}
        for each in deadends: d[each] = True

        def f(val):
            ans = []
            for z in range(len(val)):
                t1 = val[:z] + str((int(val[z])+1)%10) + val[z+1:]
                t2 = val[:z] + str((int(val[z])-1)%10) + val[z+1:]
                if t1 not in d: ans.append(str(t1))
                if t2 not in d: ans.append(str(t2))
            return ans
        
        while q and qr:
            n = q.popleft()
            nr = qr.popleft()

            for z in f(n):
                if z not in v:
                    v[z] = v[n] + 1
                    q.append(z)
                    if z in vr: return vr[z] + v[z]
            
            for z in f(nr):
                if z not in vr:
                    vr[z] = vr[nr] + 1
                    qr.append(z)
                    if z in v: return v[z] + vr[z]
                    
        return -1