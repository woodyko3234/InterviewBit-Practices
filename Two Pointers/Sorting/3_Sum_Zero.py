class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort() #O(n log(n))
        
        output = []
        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            temp = []
            while k > j:
                curSum = A[i] + A[j] + A[k]
                if curSum == 0:
                    temp = [A[i], A[j], A[k]]
                    if temp not in output:
                        output.append(temp)
                    j += 1
                    k -= 1
                elif curSum > 0:
                    k -= 1
                else: j += 1
        return output
