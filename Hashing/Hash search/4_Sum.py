from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        #create a dict to store a+b info
        sum_ab = defaultdict(list)
        n = len(A)
        for i in range(n-1):
            for j in range(i+1, n):
                sum_ab[A[i] + A[j]].append([i,j])
        
        #create another dict to store B-(a+b) info
        sum_cd = defaultdict(list)
        comb = []
        for i in range(2, n-1):
            for j in range(i+1, n):
                if sum_ab[B-(A[i]+A[j])]:
                    for k in sum_ab[B-(A[i]+A[j])]:
                        if i not in k and j not in k:
                            comb.append(tuple(sorted([A[k[0]], A[k[1]], A[i],  A[j]])))
        comb = list(set(comb))
        
        return sorted(comb)
            
