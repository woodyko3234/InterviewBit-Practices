class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        #return (x ** n) % d
        if x == 0: return x
        elif n == 0: return 1
        elif d == 1: return 0
        neg_check = 0
        if x < 0:
            x = abs(x)
            if n % 2 != 0:
                neg_check = 1
    
        r = 1
        while n > 0:
            if n & 1 == 1:
                r = r * x % d
            n = int(n/2)
            x = x * x % d
        
        if neg_check == 1:
            return d - r
        return r
    #Editorial anwser
    #def pow(self, x, n, d):
        
    #    res = 1 % d  # Cover case d == 1
    #    while n > 0:
    #        if n & 1:   # Odd?
    #           res = (res * x) % d
    #        x = x**2 % d
    #        n >>= 1
    #    return res
            
               
