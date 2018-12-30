class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        '''
        Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted, 
        then subarrays A0, …, Al-1 and Ar+1, …, AN-1 will be in sorted(ascending) order.
        '''
        '''
        Assume that Al, …, Ar is the minimum-unsorted-subarray which is to be sorted.
        then min(Al, …, Ar) >= max(A0, …, Al-1)
        and max(Al, …, Ar) <= min(Ar+1, …, AN-1)
        '''
        #eg. [2,1] => [1]
        #output: list of indices start and end
        si = -1
        ei = 0
        max1 = 0
        min1 = max(A)
        minind = -1
        for i in range(1,len(A)):
            if A[i] < A[i - 1] or A[i] < max1:
                if si == -1:
                    si = i - 1
                ei = i
                min1 = min(min1,A[i])
            max1 = max(max1,A[i])
            
        if si == -1:
            return [-1]
        else:
            for i in range(0,si):
                if A[i] > min1:
                    minind = i
                    break
            if minind < si and minind != -1:
                si = minind
            return [si,ei]
