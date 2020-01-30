class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        n = len(A)
        words = len(B)
        word_l = len(B[0])
        start_pos = False
        
        #create a dict to store words showup
        word_showed = dict()
        
        #default output: []
        output = []
        for i in B:
            try:
                word_showed[i] += 1
            except:
                word_showed[i] = 1
        
        for i in range(n):
            index = i
            testcase = word_showed.copy()
            while index <= n:
                try:
                    if testcase[A[index:index+word_l]] >= 1:
                        testcase[A[index:index+word_l]] -= 1
                        index += word_l
                    else: break
                except: break
            if sum(list(testcase.values())) == 0:
                output.append(i)
        return output
