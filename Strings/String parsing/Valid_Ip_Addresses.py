class Solution:
    # @param A : string
    # @return a list of strings
    def addressCheck(self, ip):
        for node in ip.split("."):
            if int(node) > 255:
                return False
        return True
    
    def restoreIpAddresses(self, A):
        output = []
        l = len(A)
        if l > 12 or l < 4 or (not A.isdigit()): return []
        #range from 4 to 12
        else:
            for i in range(1, l - 2):
                if i > 3: break #do not generate irrelevant combinations
                elif l - i > 9: continue #avoid generating items including more than 3 char
                elif A[0] == '0' and i > 1: break #remove "0??" conditions
                for j in range(i+1, l - 1):
                    if A[i] == '0' and j > i+1: break #remove "0??" conditions
                    elif j - i > 3: break #do not generate irrelevant combinations
                    elif l - j > 6: continue #avoid generating items including more than 3 char
                    for k in range(j+1, l):
                        if A[j] == '0' and k > j+1: break #remove "0??" conditions
                        elif A[k] == 0 and (l - k > 1): continue #remove "0??" conditions
                        elif k - j > 3: break #do not generate irrelevant combinations
                        elif l - k > 3: continue #avoid generating items including more than 3 char
                        ip = A[:i] + '.'
                        ip += A[i:j] + '.'
                        ip += A[j:k] + '.'
                        ip += A[k:]
                        if self.addressCheck(ip):
                            output.append(ip)
        return output
        
