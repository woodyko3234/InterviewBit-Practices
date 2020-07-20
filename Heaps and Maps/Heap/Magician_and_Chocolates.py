import heapq
class Solution:
    # @param T : integer, how many times the kid eat chocolates
    # @param chocs : list of integers
    # @return an integer
    def nchoc(self, T, chocs):
        total_choc = 0
        for i in range(len(chocs)):
            chocs[i] = chocs[i] * -1
        chocs = sorted(chocs)
        for _ in range(T):
            if not chocs: break
            choc = heapq.heappop(chocs)
            total_choc = (total_choc - choc) % (10**9 + 7)
            #put chocs back
            if (-choc)//2 < 1: continue
            heapq.heappush(chocs, -((-choc)//2))
        return total_choc 
