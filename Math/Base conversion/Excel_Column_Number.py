class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        a_len = len(A)
        output = 0
        if a_len == 0: return output
        
        i = a_len - 1
        times = 0
        while i >= 0:
            indice = 26*((ord(A[i])-64)//26) + (ord(A[i])-64)%26
            output += indice * (26 ** times)
            i -= 1
            times += 1
        return output
        #if a_len == 1:
        #output = 26*((ord(A)-64)//26) + (ord(A)-64)%26
        #if a_len == 2:
        #output = (26*((ord(A)-64)//26) + (ord(A)-64)%26)*26 + 26*((ord(A)-64)//26) + (ord(A)-64)%26
        
