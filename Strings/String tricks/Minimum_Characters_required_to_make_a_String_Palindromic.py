class Solution:
    # @param A : string
    # @return an integer
    def findLPS(self, s):
        n = len(s)
        rev = s[-1::-1]
        lps = [0] * (n+1)
        i, j = 0,0
        while i < n:
            if rev[i] == s[j]:
                j += 1
                i += 1
                lps[i] = j
            elif j != 0:
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
        return lps[-1]
                
    def solve(self, A):
        return len(A) - self.findLPS(A)
