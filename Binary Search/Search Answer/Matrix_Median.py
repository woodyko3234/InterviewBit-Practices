class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        min_a,max_a,n,m = A[0][0],A[0][0],len(A),len(A[0])
        for i in range(n):
            min_a = A[i][0] if A[i][0] < min_a else min_a
            max_a = A[i][-1] if A[i][-1] > max_a else max_a
        elements = (n*m+1)//2
        while min_a < max_a :
            a_mid,count = (min_a+max_a)//2,0
            for row in A:
                count += self.bisectRight(row,a_mid, 0, m)
            if count < elements:
                min_a = a_mid+1
            else:
                max_a = a_mid
        return min_a

    def bisectRight(self, lst, a_mid, start, end):
        if start == end:
            return end
        lst_counts = (start+end)//2
        if lst[lst_counts] <= a_mid:
            return self.bisectRight(lst, a_mid, lst_counts+1, end)
        else:
            return self.bisectRight(lst, a_mid, start, lst_counts)
