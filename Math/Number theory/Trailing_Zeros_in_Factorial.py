class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        #only need to count how many 5s
        if A < 5: return 0

        fives = 0
        for i in range(5, A+1, 5):
            fives += 1
        
        output = 0
        times = 1
        if fives < 5: return fives
        else:
            while fives > 0:
                output += fives
                fives  = fives // 5
                times += 1
            return output
