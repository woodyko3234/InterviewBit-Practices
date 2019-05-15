class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        splitA = list(map(int, A.split(".")))
        splitB = list(map(int, B.split(".")))
        i, j = len(splitA), len(splitB)
        min_len = min(i, j)
        for c in range(min_len):
            if splitA[c] > splitB[c]: return 1
            elif splitA[c] < splitB[c]: return -1
        if i > min_len: 
            for c in range(min_len, i):
                if splitA[c] > 0: return 1
        elif j > min_len: 
            for c in range(min_len, j):
                if splitB[c] > 0: return -1
        return 0
