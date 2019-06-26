class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        zSumSet = []
        if A.count(0) >= 3: zSumSet.append([0,0,0])
        if len(A) <= 3 or max(A) <= 0: return zSumSet
        sortA, n = sorted(A), len(A)
        for i in range(n-1, 1, -1):
            c_idx = i
            if c_idx != n-1 and sortA[c_idx] == sortA[c_idx+1]: continue
            if sortA[c_idx] <= 0: break
            b_idx, a_idx = i - 1, 0
            while b_idx > a_idx:
                if sortA[a_idx] + sortA[b_idx] == -sortA[c_idx]:
                    if (zSumSet == []) or (zSumSet[-1] != [sortA[a_idx], sortA[b_idx], sortA[c_idx]]):
                        zSumSet.append([sortA[a_idx], sortA[b_idx], sortA[c_idx]])
                    b_idx -= 1
                    a_idx += 1
                elif sortA[a_idx] + sortA[b_idx] > -sortA[c_idx]:
                    b_idx -= 1
                else: a_idx += 1
        return zSumSet
