class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self,nums):
        nums=list(nums)
        if nums==[]:
            return -1
        can1,can2,count1,count2=0,1,0,0
        for i in nums:
            if i==can1:
                count1+=1
            elif i==can2:
                count2+=1
            elif count1==0:
                can1,count1=i,1
            elif count2==0:
                can2,count2=i,1
            else:
                count1-=1
                count2-=1
        if nums.count(can1)>len(nums)/3:
            return can1
        if nums.count(can2)>len(nums)/3:
            return can2
        return -1
#from collections import Counter
#class Solution:
#    # @param A : tuple of integers
#    # @return an integer
#    def repeatedNumber(self, A):
#        a_len = len(A)
#        if a_len == 0: return -1
#        a_count = Counter(A)
#        standard = a_len/3.
#        for k, v in a_count.items():
#            if v > standard:
#                return k
#        return -1
