class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        #split with "/"
        a_len = len(A)
        if a_len == 0: return A
        a_split = A.split('/')
        
        #if one space shows up, discard all the items after!!!
        n = len(a_split)
        for i in range(n):
            if a_split[i] != a_split[i].split(' ')[0]:
                a_split[i] = a_split[i].split(' ')[0]
                a_split = a_split[:i]
                break
        
        i = len(a_split)-1
        pop_next = 0
        while i > 0:
            if a_split[i] == '..':
                pop_next += 1
                a_split.pop(i)
            elif a_split[i] == '' or a_split[i] == '.':
                a_split.pop(i)
            elif pop_next > 0:
                a_split.pop(i)
                pop_next -= 1
            i -= 1
        return '/'.join(a_split) or '/'
