class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def __init__(self):
        self.output = []
        
    def combine(self, n, k, pos = 0, temp = None):
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
        temp = temp or []
        if len(temp) == k:
            self.output.append(temp[:])
            return 
        for i in range(pos, n):
            temp.append(pos+1)
            self.combine(n, k, i+1, temp)
            temp.pop()
        
        return self.output
