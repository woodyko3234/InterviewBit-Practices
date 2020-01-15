from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        addition = defaultdict(list)
        n = len(A)
        for i in range(0, n-1):
            duplicates = defaultdict(bool)
            for j in range(i+1, n):
                if not duplicates[A[j]]:
                    try:
                        if i == addition[A[i]+A[j]][-1] or i == addition[A[i]+A[j]][-1][-1]: continue
                    except: pass
                    try:
                        if j == addition[A[i]+A[j]][-1] or j == addition[A[i]+A[j]][-1][-1]: continue
                    except: pass
                    addition[A[i]+A[j]].append([i, j])
                    duplicates[A[j]] = True
                else: continue
                    
        
        a = float('inf')
        values = list(addition.values())
        for i in range(len(values)):
            length = len(values[i])
            if length > 1:
                if a > values[i][0][0]:
                    a,b,c,d = values[i][0][0], values[i][0][1], values[i][1][0], values[i][1][1]
                elif a == values[i][0][0] and b > values[i][0][1]:
                    b,c,d = values[i][0][1], values[i][1][0], values[i][1][1]
                elif a == values[i][0][0] and b == values[i][0][1] and c > values[i][1][0]:
                    c,d = values[i][1][0], values[i][1][1]
                elif a == values[i][0][0] and b == values[i][0][1] and c == values[i][1][0] and d > values[i][1][1]:
                    d = values[i][1][1]
            else: continue
        
        if a != float('inf'):
            return [a,b,c,d]
        else:
            return []
