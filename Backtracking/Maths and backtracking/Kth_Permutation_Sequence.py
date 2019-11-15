class Solution:
    # @param n : integer
    # @param k : integer, must be less than n! and greater than 0
    # @return a strings
    def __init__(self):
        self.output = ""
        
    def factorial(self, n, facList):
        """
        apply a list to store those factorials, avoiding duplicated computations.
        """
        if n > 1:
            if facList[-n] == -1:
                facList[-n] = n * self.factorial(n-1, facList)
            return n*self.factorial(n-1, facList)
        else: 
            if facList[-n] == -1:
                facList[-n] = n
            return n
        
    def getPermutation(self, n, k):
        '''
        example: arr = [1,2,3], n = 3
        3 choice for index_0
        2 for index_1
        1 for index_2 (no choice)
        so total permutations = 3! = 6
        if k = 4
        index0 = arr.pop((k-1) // (n-1)!) #3//2 = 1, arr.pop(1) = 2, arr := [1,3]
        new k = k - (n-1)! * popped_idx #4-2*1 = 2
        index1 = arr.pop((k-1) // (n-1)!) #1//1 = 1, arr.pop(1) = 3, arr := [1]
        if len(arr) == 1: index_-1 = arr.pop()
        
        how about arr = [1,2,3,4] n = 4 and k = 10?
        index0 = arr.pop((k-1) // (n-1)!) #9//6 = 1, arr.pop(1) = 2, arr := [1,3,4]
        new k = k - (n-1)! * popped_idx #10-6*1 = 4 new n = 3
        index1 = arr.pop((k-1) // (n-1)!) #3//2 = 1, arr.pop(1) = 3, arr := [1,4]
        new k = k - (n-1)! * popped_idx #4-2*1 = 2 new n = 2
        index2 = arr.pop((k-1) // (n-1)!) #1//1 = 1, arr.pop(1) = 4, arr := [1]
        ans:2341
        '''
        if n == 1: return "1"
        arr = [str(i+1) for i in range(n)]
        facList = [-1] * (n-1)
        self.factorial(n-1, facList)
        facList = facList[::-1]
        def loopFunc(arr, k, facList):
            while arr and facList:
                fac_val = facList.pop()
                idx = (k-1) // fac_val
                self.output += arr.pop(idx)
                k -= fac_val * idx
            self.output += arr.pop()
        
        loopFunc(arr, n, k, facList)
        return self.output
