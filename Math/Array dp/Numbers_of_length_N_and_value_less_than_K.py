class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def get_count(self, A, B, base, index):
        if index >= len(base) or B==0:
            return 1
        current_max = int(base[index])
        rt = 0
        for x in A:
            if index == 0 and x ==0 and B!=1:
                continue
            if x > current_max:
                continue
            if x == current_max:
                if index >= len(base) -1:
                    continue
                rt = rt + self.get_count(A, B-1, base, index+1)
            else:
                rt = rt + len(A)**(B-1)
        return rt
                
    
    def solve(self, A, B, C):
        base = str(C)
        if len(base) < B:
            return 0
        
        index = 0
        if len(base) == B:
            return self.get_count(A, B, base, 0)
        rt = 0
        for x in A:
            if x == 0 and B!=1:
                continue
            if x==0 and x < C:
                rt +=1
            else:
                rt = rt + len(A)**(B-1)
        return rt
            
