from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #for example A = [0,1,2,3,4]
        #when p = 0, no. of integers greater than p = 4
        #when p = 1, no. of integers greater than p = 3
        #when p = 2, no. of integers greater than p = 2
        #when p = 3, no. of integers greater than p = 1
        #when p = 4, no. of integers greater than p = 0
        a_len = len(A)
        a_count = Counter(A)
        a_sort = sorted(a_count.items(), key = lambda k: k[0])
        item_left = a_len
        for p, num in a_sort:
            item_left -= num
            if p == item_left: return 1
        return -1
