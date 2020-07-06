class Solution:
    # @param H : list of integers
    # @param I : list of integers
    # @return a list of integers
    def order(self, H, I):
        """
        return the correct Height’s array that matches the constrains 
        given by the Infronts array.
        e.g. Height   [5 3 2 6 1 4]
             Infronts [1 0 2 0 3 2]
        output [3 6 2 1 5 4]
        """
        N = len(H)
        data = {H[i]:I[i] for i in range(N)}
        
        positions = list(range(N))
        
        res = [None] * N
        
        for k in sorted(data.keys()):
            res[positions[data[k]]] = k
            del positions[data[k]]
        
        return res
