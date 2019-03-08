import sys
sys.setrecursionlimit(5000)

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def calc_combs(self, length, combinations, interval_l, interval_c, memo):
        return combinations * interval_c * self.fact(length + interval_l, memo) // (self.fact(length, memo) * self.fact(interval_l, memo))

    def fact(self, n, memo):
        try: 
            memo[n]
            return memo[n]
        except: pass
        if n <= 1: return 1
        v = self.fact(n - 1, memo) * n
        memo[n] = v
        return v
    def solve(self, A, B):
        if not B: return 0 #can not start
        mod = 1000000007 #modulo
        memo = {} # dict
        B = sorted(B) #may be unsorted

        # 1...B[0] has 1 possible placements of length B[0] - 1
        length, combinations = B[0] - 1, 1

        for i in range(1, len(B)):
            #if B[i - 1] == B[i]: continue #duplicates check
            if B[i - 1] + 1 == B[i]: continue #continuous that no need to check separatedly
            interval_l = (B[i] - B[i - 1] - 1) % mod
            interval_c = (1 << (interval_l - 1)) % mod #move 1 bitwise to its left; 
            #c is the total combinations within the interval, since it can only choose from left or right side
            #so should be 2^(l-1)
            combinations = self.calc_combs(length, combinations, interval_l, interval_c, memo) % mod
            #why do we need to multiply length and combinations with current calculation again?
            #since we did not take the later combinations into considerations when computing the previous intervals
            length += interval_l

        # B[-1]...A has 1 possible placements of length A - B[-1]
        return self.calc_combs(length, combinations, A - B[-1], 1, memo) % mod
