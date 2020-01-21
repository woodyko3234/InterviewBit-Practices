from collections import defaultdict, Counter
class Solution:
    # @param S : string
    # @param T : string
    # @return a strings
    def minWindow(self, S, T):
        if len(T) > len(S): return ""
        tCounter = Counter(T)
        sPos = defaultdict(list)
        n, m = len(S), len(T)
        minlen, startP = n+1, -1
        output = ""
        for i in range(n):
            if tCounter[S[i]] >= 1:
                tCounter[S[i]] -= 1
                m -= 1
                sPos[S[i]].append(i)
                if startP < 0:
                    startP = i
            elif sPos[S[i]] == []: continue
            else:
                pos = sPos[S[i]].pop(0)
                sPos[S[i]].append(i)
                if pos > startP: continue
            #m > 0 means there's no such fitting substring yet
            if m > 0: continue
            find_newS = []
            for val in sPos.values():
                if not val: continue
                find_newS.append(val[0])
            startP = min(find_newS)
            if minlen > (i - startP + 1):
                minlen = (i - startP + 1)
                output = S[startP: i+1]
        return output
