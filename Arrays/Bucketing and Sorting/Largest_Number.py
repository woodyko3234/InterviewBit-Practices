class Num:
    def __init__(self, v):
        self.val = str(v)
    
    def __lt__(self, other):
        return self.val + other.val < other.val + self.val
    
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        num_list = []
        for i in A:
            num_list.append(Num(i))
        
        num_list.sort(reverse=True)
        
        output = []
        for i in num_list:
            output.append(i.val)
        
        if output[0][0] == '0':
            output = ['0']
        
        return(''.join(output))
