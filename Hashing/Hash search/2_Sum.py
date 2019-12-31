class Solution:
    # @param A : tuple of integers
    # @param T : integer
    # @return a list of integers
    def twoSum(self, A, T):
        idxHash = dict()
        output = []
        for i in range(len(A)):
            try:
                output = [idxHash[A[i]]+1, i+1]
                break
            except:
                try:
                    idxHash[T-A[i]]
                    continue
                except:
                    idxHash[T-A[i]] = i
        return output
