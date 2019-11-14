class Solution:
    # @param n : integer
    # @return a list of integers
    def __init__(self):
        self.output = []
    def grayCode(self, n):
        def recursive(n, res = ["0", "1"]):
            res = res or ["0", "1"]
            if n == 1: 
                self.output.extend(res)
            else:
                recursive(n-1, ["0" + i for i in res]+["1" + j for j in res[::-1]])
        recursive(n, ["0", "1"])
        return [int(i, 2) for i in self.output]
