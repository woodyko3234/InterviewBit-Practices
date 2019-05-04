class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        for c in set(A):
            if c.isalnum(): continue
            else: A = A.replace(c, " ")
        test_str = "".join(A.split(" ")).lower()
        
        l = len(test_str)
        if l % 2 == 0:
            mid = l // 2 - 1
        else:
            mid = l // 2
        #test
        for i in range(mid + 1):
            if test_str[i] != test_str[l-1 - i]:
                return 0
        return 1
