class Solution:
	# @param A : list of strings
	# @param B : integer
	# @return a list of strings
	def fullJustify(self, A, B):
	    if not A: return A
	    length_A = [len(i) for i in A]
	    sentences = []
	    temp, temp_l = [], 0
	    for i, l in zip(A, length_A):
	        #each word is guaranteed not to exceed B.
	        if temp == []:
	            temp.append(i)
	            temp_l += l
	        elif (temp_l + 1 + l) <= B:
	            temp.append(i)
	            temp_l += 1 + l
	        else:
	            #check how many blanks we need
	            sentence = self.blankAllocate(temp, temp_l, B)
	            sentences.append(sentence)
	            temp, temp_l = [], 0
	            temp.append(i)
	            temp_l += l
	    sentence = " ".join(temp)
	    sentence += " " * (B - len(sentence))
        sentences.append(sentence)
	    return sentences
    
    def blankAllocate(self, temp, temp_l, B):
        blank_intervals = len(temp) - 1
        total_blanks = B - (temp_l - blank_intervals)
        if blank_intervals > 0:
            base_blanks = total_blanks // blank_intervals
            if base_blanks * blank_intervals != total_blanks:
                adding_blanks = total_blanks % blank_intervals
            else: adding_blanks = 0
        else: 
            base_blanks = B - temp_l
            adding_blanks = 0
        sentence = ""
        if len(temp) == 1: return temp[0] + " " * base_blanks
        for w in temp:
            if sentence == "":
                sentence += w
            elif adding_blanks > 0:
                sentence += (" " * (base_blanks + 1)) + w
                adding_blanks -= 1
            else:
                sentence += (" " * (base_blanks)) + w
        return sentence
