from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        a_len = len(A)
        if a_len == 0: return -1
        a_count = Counter(A)
        standard = a_len/3.
        for k, v in a_count.items():
            if v > standard:
                return k
        return -1
