class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        target = A.lower()
        vowel = ['a','e','i','o','u']
        amazing_num, l = 0, len(A)
        for idx, i in enumerate(target):
            if i in vowel:
                amazing_num += (l - idx)
        return amazing_num % 10003
