class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        maxPos, minNeg = [], []
        n = len(A)
        if n < 3: return 
        elif n == 3: return A[0]*A[1]*A[2]
        minPro = []
        for i in A:
            if i >= 0:
                if len(maxPos) < 3:
                    maxPos.append(i)
                else:
                    maxPos.sort()
                    if maxPos[0] < i:
                        maxPos[0] = i
            else:
                if len(minNeg) < 2:
                    minNeg.append(i)
                else:
                    minNeg.sort()
                    if minNeg[-1] > i:
                        minNeg[-1] = i
                if len(minPro) < 3:
                    minPro.append(i)
                else:
                    minPro.sort()
                    if abs(i) < minPro[0]:
                        minPro[0] = i
        products = sorted(maxPos)
        #condition: 3 neg
        if len(products) == 0:
            products = minPro
        #condition: 2 Neg, 1 Pos
        elif len(products)==1:
            products += minNeg
        #condition: 3 pos or (2 Neg, 1 Pos)
        elif len(products) > 1 and len(minNeg) == 2:
            if minNeg[0]*minNeg[1] > products[0]*products[1]:
                return max(products) * minNeg[0]*minNeg[1]
        #condition: 2 pos 1 neg, only happened when there are only 3 elements
        #covered with if (n == 3) condition
        #should only consider 0
        products.sort(reverse = True)
        return products[0] * products[1] * products[2]
