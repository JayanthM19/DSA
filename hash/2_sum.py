#https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq={}

        for i,num in enumerate(nums):
            rem = target - num

            if rem in freq:
                return [freq[rem],i]
            
            freq[num]=i