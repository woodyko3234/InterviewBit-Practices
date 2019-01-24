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
        si = -1
        ei = 0
        max1 = 0
        min1 = max(A)
        i, l = 1, len(A)
        while i < l:
            if A[i] >= A[i-1]: i += 1
            else:
                ei = i
                for j in range(0, i):
                    if A[j] > A[ei]:
                        si = j
                        break
                max1 = max(A[si:ei+1])
                min1 = min(A[si:ei+1])
                for i in range(i+1, l):
                    if A[i] < max1: 
                        ei = i
                        if A[i] < min1: min1 = A[i]
                    else: max1 = A[i]
                for j in range(0, si):
                    if A[j] > min1:
                        si = j
                        break
                break
        if si == -1: return [si]
        return [si, ei]
                        
                        
                        
