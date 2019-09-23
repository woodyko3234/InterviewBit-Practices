class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A, sort = True):
        """
        If built with loops will be like......
        output, n = [[]], len(A)
        for i in range(n):
            output.append([A[i]])
            for j in range(i+1, n):
                output.append([A[i], A[j]])
                for k in range(j+1, n):
                    output.append([A[i], A[j], A[k]])
                    for l in range(k+1, n):
                        ......
                        ......
        return output
        So what's the condition while recursion is called?
        iterated parameters: 
            indexes in the list(i, j, k, l......)
            the list(A)
        """
        if sort: A.sort()
        yield []
        for i in range(len(A)):
            for subset in self.subsets(A[i+1:], sort = False):
                yield [A[i]] + subset
