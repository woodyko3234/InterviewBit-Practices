import heapq
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        res=[]
        A.sort()
        res.append(A[0][1])
        
        for i in range(1,len(A)):
            
            
            temp=heapq.heappop(res)
            if A[i][0]>=temp:
                heapq.heappush(res,A[i][1])
            else:
                heapq.heappush(res,temp)
                heapq.heappush(res,A[i][1])
            #res.sort(reverse=True)
            
        return len(res)
