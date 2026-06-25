#https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        for key,val in freq.items():
            if val==1:
                return key