class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if len(A) == 0: return 0
        word_list = A.split(' ')
        for i in word_list[::-1]:
            if len(i) > 0:
                return len(i)
        return 0
