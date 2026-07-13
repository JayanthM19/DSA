#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return sum(nums[i-1]>nums[i] for i in range(len(nums)))<2
        