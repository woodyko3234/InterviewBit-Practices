class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        times = 2
        if B == 0 and A == 0: return 0
        elif B > 0 and A%B == 0: return B
        elif A > 0 and B%A == 0: return A
        minimum = min(A, B)
        
        gcd = 1
        while times <= int(minimum):
            if times // 5 > 1 and times % 5 == 0: times += 2 
            elif A % times == 0 and B % times == 0:
                gcd *= times
                A /= times
                B /= times
                minimum /= times
            else: 
                if times == 2: times += 1
                else: times += 2
        return gcd
