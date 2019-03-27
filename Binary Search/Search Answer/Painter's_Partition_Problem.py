class Solution:
    # @param K : integer
    # @param T : integer
    # @param L : list of integers
    # @return an integer
    def isPossible(self, L, mid):
        painters = 1
        pt = 0
        for p in L:
            if (pt + p) <= mid:
                pt += p
            else:
                pt = p
                painters += 1
        return painters
    
    def paint(self, K, T, L):
        tl = sum(L)
        worst = tl
        best = max(L)
        if K == 1: return (worst * T) % 10000003
        while best < worst:
            mid = (worst+best)//2
            painters = self.isPossible(L, mid)
            if painters <= K:
                worst = mid
            else:
                best = mid + 1
        return (best * T) % 10000003
