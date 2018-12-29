class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 0: return [1]
        num = A
        while len(num) > 0 and num[0] == 0:
            num.remove(0)
        digits = len(num)
        if digits == 0: return [1]
        i = -1
        num[i] = num[i] + 1
        while num[i] % 10 == 0 and i + digits > 0:
            num[i] = 0
            num[i-1] += 1
            i -= 1
        if num[0] % 10 == 0:
            num[0] = 0
            num = [1] + num
        
        return num
