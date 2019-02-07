from math import sqrt
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, n):
        if n > 2**32: return 0
        elif n == 1: return 1
        numbers = []

        # add all square numbers from 1 <= a <= sqrt(n) 
        # but only if n is multiple of a 
        for a in range(2, int(sqrt(n)) + 1):
            if (n % a == 0):
                numbers.append((a, a * a))

        # check list of candidates 
        while numbers:
            # pop last tuple, see if we have n or whether n can be made 
            (a, x) = numbers.pop()
            e = 2
            # try to compose n with a^e with e := integer greater than 1 
            while x < n:
                e += 1
                x *= a
            if x == n:
                return 1
        # no solution was found looking at the candidates 
        return 0
