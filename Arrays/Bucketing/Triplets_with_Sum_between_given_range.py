class Solution:
    # @param A : list of strings
    # @return an integer

    def solve(self, A):
        n = len(A)
        B = [float(i) for i in A]
        buckets = [[], [], []]
        for i in B:
            if i < 2.0/3:
                buckets[0].append(i)
            elif i < 1:
                buckets[1].append(i)
            else:
                buckets[2].append(i)
        
        def get(index):
            amx1, amx2, amx3 = -10, -10, -10
            ami1, ami2, ami3 = 3, 3, 3
            for i in buckets[index]:
                if i > amx1:
                    amx1, amx2, amx3 = i, amx1, amx2
                elif i > amx2:
                    amx2, amx3 = i, amx2
                elif i > amx3:
                    amx3 = i
            
                if i < ami1:
                    ami1, ami2, ami3 = i, ami1, ami2
                elif i < ami2:
                    ami2, ami3 = i, ami2
                elif i < ami3:
                    ami3 = i
            return [amx1, amx2, amx3, ami1, ami2, ami3]
        
        
        a = get(0)
        b = get(1)
        c = get(2)
        ls = []
        #AAA condition
        fc = a[0] + a[1] + a[2]
        ls.append(fc)
        #AAC
        fc = a[3] + a[4] + c[3]
        ls.append(fc)
        fc = a[3] + b[3] + b[4]
        ls.append(fc)
        fc = a[3] + b[3] + c[3]
        ls.append(fc)
        #AAB condition
        fc = b[0] + a[3] + a[4]
        ls.append(fc)
        if a[0] != a[3]:
            #AAB
            fc = b[0] + a[0] + a[3]
            ls.append(fc)
            #AAB
            fc = b[3] + a[0] + a[3]
            ls.append(fc)
        #AAB
        fc = b[3] + a[0] + a[1]
        ls.append(fc)
        for fc in ls:
            if fc > 1 and fc < 2:
                return 1
        return 0
