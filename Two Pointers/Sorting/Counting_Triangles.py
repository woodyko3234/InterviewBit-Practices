class Solution:
    # @param A : list of integers
    # @return an integer

    def nTriang(self, A):
        n = len(A)
        A.sort()
        count = 0
 
        for i in range(0,n-2):
            k = i + 2
            for j in range(i+1,n):
                while (k < n and A[i] + A[j] > A[k]):
                    k += 1
                count += k - j - 1
     
        return count % 1000000007
