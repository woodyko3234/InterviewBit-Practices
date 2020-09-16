from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        stat = Counter(A)
        n = len(A) // 2
        for k, v in stat.items():
            if v > n:
                return k
        return None
