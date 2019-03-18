class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self,A,B):
        if(len(A)<B):
            return -1
        if(len(A)==B):
            return max(A)
        return self.findsol(A,B)

    def findsol(self,A,B):
        start=0
        end=sum(A)
        res=sys.maxsize
        while(start<=end):
            mid=int(start+(end-start)/2)
            x=self.ispossible(mid,A,B)
            #print(mid,x)
            if(x==1):
                res=min(mid,res)
                end=mid-1
            else:
                start=mid+1
        return res
    
    def ispossible(self,x,A,B):
        curmin=0
        nos=1    #number of students required
        for i in range(len(A)):
            if(A[i]>x):
                return 0
            if(curmin+A[i]>x):
                curmin=A[i]
                nos+=1
                if(nos>B):
                    return 0
            else:
                curmin+=A[i]
        return 1
