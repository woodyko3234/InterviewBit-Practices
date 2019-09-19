class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        """
        Find nearest element which is less than the current element and on its left.
        """
        gL = [-1]
        smaller = [A[0]]
        for i in A[1:]:
            notAppended = True
            j = len(smaller) - 1
            while j >= 0:
                if i > smaller[j]:
                    gL.append(smaller[j])
                    smaller.append(i)
                    notAppended = False
                    break
                else:
                    smaller.pop()
                    j -= 1
            if notAppended:
                gL.append(-1)
                smaller.append(i)
        return gL
