class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) == 1:
            return [A]
        perms = []
        for digit in A:
            remaining_digits = A[:]
            remaining_digits.remove(digit)
            for rem_perm in self.permute(remaining_digits):
                perms.append([digit] + rem_perm)
        return perms
