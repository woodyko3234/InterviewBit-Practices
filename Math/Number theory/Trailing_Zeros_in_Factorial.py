class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        if A < 5: return 0
        power = 1
        zeros = 0
        while pow(5, power) <= A:
            zeros += A//pow(5, power)
            power += 1
        return zeros
