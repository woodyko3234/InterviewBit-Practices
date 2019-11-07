class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        """
        output = []
        num_list = [ i for i in range(1, A+1)]
        #create as many loops as B states
        for i in range(A-B):
            for j in range(i+1, A-B+1):
                for k in range(j+1, A-B+2):
                    ......
                        output.append([A[i], A[j], A[k], A[......]])
        return output
        """
        return self.x(1, A, B)
    
    def x(self, start, end, length):
        if length == 0:
            return [[]] # only one combination for k=0
        if end - start + 1 < length:
            return [] # no combination possible
        result = []
        for i in range(start, end + 1):
            for e in self.x(i + 1, end, length - 1):
                result.append([i] + e)
        return result
