class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        a_lower = A.lower()
        a_list = list(a_lower)
        a_len = len(a_list)
        for i in range(a_len):
            if  (97 <= ord(a_list[i]) <= 122) or (48 <= ord(a_list[i]) <= 57): 
                continue
            else: 
                a_list[i] = ''
        a_lower = ''.join(a_list) #update content
        a_len = len(a_lower) #update length
        
        left = 0
        right = a_len -1
        while left <= right:
            if a_lower[left] != a_lower[right]:
                return 0
            else: 
                left += 1
                right -= 1
        
        return 1
