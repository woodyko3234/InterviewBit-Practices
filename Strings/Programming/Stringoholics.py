class Solution:
    # @param A : list of strings
    # @return an integer
    def gcd(self, a, b):
        if b > a:
            a, b = b, a
        if b == 0: return a
        return self.gcd(b, a%b)
    
    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
    
    def computeLPSArray(self, pat):
        m = len(pat)
        lps = [0]*m
        i, j = 1,0
        while i < m:
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
        res_num = lps[-1]
        if m % (m-res_num) == 0: return m-res_num
        else: return m

    def solve(self, A):
        n = len(A)
        ans = 1
        for s in A:
            res = self.computeLPSArray(s)
            for i in range(1, 2*res+1):
                if ((i*(i+1))//2)%res == 0:
                    ans = self.lcm(ans, i)
                    break
        return ans % 1000000007
                
