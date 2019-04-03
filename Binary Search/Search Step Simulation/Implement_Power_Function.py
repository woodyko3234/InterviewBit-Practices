class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if d == 1: return 0
        elif x == 0: return x
        elif n == 0: return 1
        elif n == 1: return x % d
        r = x % d
        oddP=[]
        while n >= 2:
            if n % 2 == 1:
                oddP.append(r)
            r = (r**2) % d
            n //= 2
        for i in oddP:
            r = (r * i) % d
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
            
               
