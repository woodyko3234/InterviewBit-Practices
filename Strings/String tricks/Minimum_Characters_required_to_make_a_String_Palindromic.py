class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        rever_str = A[::-1]
        remove_count = 0
        while remove_count < len(A):
            idx = 0
            fits = True
            for char in rever_str[remove_count:]:
                if A[idx] != char:
                    fits = False
                    break
                idx += 1
            if fits:
                return remove_count
            else:
                remove_count += 1
            
        return remove_count
