class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        hashmap = {}
        elements = list(str(A))
        n = len(elements)
        for i in range(n):
            temp = int(elements[i])
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
