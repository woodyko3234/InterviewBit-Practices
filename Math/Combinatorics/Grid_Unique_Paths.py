import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        steps_right = A - 1
        steps_down = B - 1
        fr = math.factorial(steps_right)
        fd = math.factorial(steps_down)
        ft = math.factorial(steps_right + steps_down)
        # print(fr, fd, (fr + fd), (fr * fd))
        return ft // (fr * fd)
