class Solution:
    # @param M : list of integers, positions of mice
    # @param H : list of integers, positions of Holes
    # @return an integer
    def mice(self, M, H):
        #Think we can just apply sorting?!
        M.sort()
        H.sort()
        n = len(M)
        minMins = 0
        for i in range(n):
            if abs(M[i] - H[i]) > minMins:
                minMins = abs(M[i] - H[i])
        return minMins
