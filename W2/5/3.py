# 127
# https://leetcode.com/problems/x-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList = [beginWord] + wordList
        d = {}
        size = len(beginWord)
        for x in wordList:
            for z in range(size):
                k = x[:z]+'*'+x[z+1:]
                d[k] = ( d[k]  if k in d else []) + [x]        

        q, s, ans = deque([beginWord]), set([beginWord]), 0
        while len(q):
            for z in range(len(q)):
                c = q.popleft()
                if(c==endWord): return ans+1
                for z in range(size):
                    k = c[:z]+'*'+c[z+1:]
                    for y in d[k]:
                        if y not in s:
                            q.append(y)
                            s.add(y)
            ans+=1   
        return 0