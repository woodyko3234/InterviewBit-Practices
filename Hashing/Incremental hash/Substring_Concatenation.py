from collections import Counter
class Solution:
    # @param S : string
    # @param L : tuple of strings
    # @return a list of integers
    def findSubstring(self, S, L):
        strCounter = Counter(L)
        sl, wl, n = len(S), len(L[0]), len(L)
        ll = wl * n
        output = []
        for i in range(sl):
            temp = strCounter.copy()
            idx = i
            if (sl-i) < ll: break
            while temp[S[idx:idx+wl]]>0:
                temp[S[idx:idx+wl]] -= 1
                idx += wl
            if sum(temp.values()) == 0:
                output.append(i)
        return output
