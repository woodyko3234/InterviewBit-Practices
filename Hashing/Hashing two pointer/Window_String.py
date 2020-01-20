from collections import defaultdict, Counter
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if len(A) < len(B): return ""
        
        target_counter = Counter(B)
            
        n = len(A)
        start = -1
        maxl = n + 1
        output = ""
        positions = defaultdict(list)
        target_l = len(B)
        for i in range(n):
            try:
                if target_counter[A[i]] >= 1: 
                    target_counter[A[i]] -= 1
                    target_l -= 1
                    positions[A[i]].append(i)
                    if start < 0:
                        start = i
                    if target_l == 0 and maxl > (i - start + 1):
                        maxl = (i - start + 1)
                        output = A[start: i+1]
                else:
                    if positions[A[i]][0] != start:
                        positions[A[i]].append(i)
                        positions[A[i]].pop(0)
                    else:
                        #recalculate start and maxl
                        positions[A[i]].append(i)
                        positions[A[i]].pop(0)
                        new_s = []
                        for j in list(positions.values()):
                            if len(j) > 0:
                                new_s.append(j[0])
                        start = min(new_s)
                        if target_l == 0 and maxl > (i - start + 1):
                            maxl = (i - start + 1)
                            output = A[start: i+1]
                        
            except: continue
            #print(output)
        return output
