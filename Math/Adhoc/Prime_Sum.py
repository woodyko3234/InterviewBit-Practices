class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        sieve = [True]*(A+1)
        sieve[1] =False;
        sieve[0] = False
        i = 2
        while(i*i <= A):
            if(sieve[i]):
                for j in range( i*2 , A+1 , i):
                    sieve[j] = False
            i+=1
        ele = A // 2
        found = False
        one = 0
        two = 0
        while(ele != 2 or not found):
            if(sieve[ele] and sieve[A - ele]):
                found = True
                one = ele
                two = A - ele
            ele -= 1
        return [one,two]
