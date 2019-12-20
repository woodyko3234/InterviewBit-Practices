class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        hashmap = {}
        elements = list(str(A))
        n = len(elements)
        if n > 8 or (len(set(elements)) != len(elements)): return 0
        elif n == 1: return 1
        for i in range(n):
            temp = int(elements[i])
            if temp == 0 or temp == 1: return 0
            try:
                if hashmap[temp]: return 0
            except:
                hashmap[temp] = True
            for j in map(int, elements[i+1:]):
                temp *= j
                try:
                    if hashmap[temp]: return 0
                except:
                    hashmap[temp] = True
        return 1
