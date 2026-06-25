#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                nums[k]=nums[i]
                k+=1
        
        nums[k]=nums[n-1]
        k+=1
        
        return k