class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, n, k):
        '''
        example arr[1,2,3], n = 3
        3 choice for index_0
        2 for index_1
        1 for index_2 (no choice)
        if k = 4
        index0 = n.pop((k-1) // (n-1)!) #3//2 = 1, n.pop(1) = 2, n := [1,3]
        new k = k - (n-1)! * pop_val #4-2*2 = 2
        index1 = n.pop((k-1) // (n-1)!) #1//1 = 1, n.pop(1) = 3, n := [1]
        if len(n) == 1: index_-1 = *n
        
        how about arr[1,2,3,4] n = 4 and k = 10?
        index0 = n.pop((k-1) // (n-1)!) #9//6 = 1, n.pop(1) = 2, n := [1,3,4]
        new k = k - (n-1)! * pop_val #10-6*1 = 4 new n = 3
        index1 = n.pop((k-1) // (n-1)!) #3//2 = 1, n.pop(1) = 3, n := [1,4]
        new k = k - (n-1)! * pop_val #4-2*1 = 2 new n = 2
        index2 = n.pop((k-1) // (n-1)!) #1//1 = 1, n.pop(1) = 4, n := [1]
        ans:2341
        '''
        #How can we solve it without applying factorial???
        array = list(map(str,range(1, n+1)))
        output = ""
        combinations = 1
        new_k = k
        l = len(array)
        def factorial(A):
            if A == 0:
                return 1
            return A*factorial(A-1)
        combinations = factorial(n-1)
        while l > 1:
            pop_val = int((new_k-1) // (combinations))
            output+=array[pop_val]
            array.remove(array[pop_val])
            new_k -= combinations * pop_val
            l -= 1
            combinations = int(combinations / l) 
            #apply int to avoid it become float when testing with long numbers 
        output += array[0]
        return output
        
