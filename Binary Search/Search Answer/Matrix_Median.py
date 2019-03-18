class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        B=[]
        for i in range(0,len(A)):
            for j in A[i]:
                B.append(j)
        B.sort()
        #print(B)
        if len(B)%2==0:
            median=(B[len(B)//2]+B[len(B)//2-1])//2
        else:
            median=B[(len(B)-1)//2]
        return median
