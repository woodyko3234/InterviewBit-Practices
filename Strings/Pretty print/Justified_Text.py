class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        w_count = len(A)
        if w_count == 0: return []
        w_combine = []
        limits = 0
        idx = 0
        sentence = ""
    
        while idx < w_count:
            if limits == 0:
                sentence += A[idx]
                limits += len(A[idx])
                idx += 1
            elif limits + 1 + len(A[idx]) <= B:
                sentence = sentence + ' ' + A[idx]
                limits += (1+len(A[idx]))
                idx += 1
            else:
                if limits == B: pass
            
                else:
                    section = sentence.split(' ')
                    sen_len = sum(len(i) for i in section)
                    if len(section) == 1:
                        spaces = ' ' * (B - sen_len)
                        sentence = section[0] + spaces
                    elif (B - sen_len) % (len(section) - 1) == 0:
                        spaces = ' ' * ((B - sen_len) / (len(section) - 1))
                        sentence = spaces.join(section)
                    else:
                        left_times = (B - sen_len) % (len(section) - 1)
                        left_spaces = ' ' * (((B - sen_len) / (len(section) - 1)) + 1)
                        right_times = (len(section) - 1) - left_times
                        right_spaces = ' ' * ((B - sen_len) / (len(section) - 1))
                        sentence = ''
                        for i in range(len(section)):
                            sentence += section[i]
                            if left_times > 0:
                                sentence += left_spaces
                                left_times -= 1
                            elif right_times > 0:
                                sentence += right_spaces
                                right_times -= 1
                            else: pass
                w_combine.append(sentence)
                sentence = ""
                limits = 0
        if limits < B:
            sentence += ' ' * (B - limits)
        w_combine.append(sentence)
        return w_combine
                        
