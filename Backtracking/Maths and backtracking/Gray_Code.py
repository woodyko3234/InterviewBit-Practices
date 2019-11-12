class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        res = []
        for _ in range(A):
            cur_res = res[::] if res else ['']
            res = ['0' + x for x in cur_res]
            res.extend('1' + x for x in cur_res[::-1])
        return [int(x, 2) for x in res]
