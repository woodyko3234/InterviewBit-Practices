class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low = 1
        high = A//2
        if A <= 1: return A
        
        while low <= high:
            mid = (low + high)//2
            midsqr = mid * mid
            if midsqr < A:
                low = mid + 1
            elif midsqr > A:
                high = mid - 1
            else: return mid
            
        return (low + high)//2
