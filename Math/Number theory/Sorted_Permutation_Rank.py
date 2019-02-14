from math import factorial
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        rank = 1
        letters = sorted(list(A))
        for i, c in enumerate(A):
            pos = letters.index(c)
            letters.remove(c)
            rank += pos * factorial(len(letters))
            if rank > 1000003:
                rank = rank % 1000003
        return rank
