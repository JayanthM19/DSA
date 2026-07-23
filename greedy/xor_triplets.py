#https://leetcode.com/problems/number-of-unique-xor-triplets-i/
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        n=len(nums)
        if n<=2:
            return n
        
        mask = 0
        for num in nums:
            mask |= num
        
        return mask+1