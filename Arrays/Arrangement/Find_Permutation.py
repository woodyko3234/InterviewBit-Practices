from collections import Counter
class Solution:
    # @param A : string only consist of 'D' and 'I'
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        #Length of given string s will always equal to n - 1
        #D means the next number is smaller, while I means the next number is greater.
        #output: nth integers in a list
        #s = 'DDI'
        #n = 4
        #1st > 2nd > 3rd < 4th
        s = [A[0]] + list(A)
        s_count = Counter(s)
        output = [0]*B
        idx = 0
        min_max = (B + 1)-s_count['I']
        max_min = 0+s_count['D']
    
        while idx < B:
            if s[idx] == 'D' :
                output[idx] = max_min
                max_min -= 1
            elif s[idx] == 'I':
                output[idx] = min_max
                min_max += 1
            idx += 1
        return output
