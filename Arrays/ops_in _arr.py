#https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        n=len(nums)


        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
            
        
        
        k=0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        
        while k < n:
            nums[k] = 0
            k += 1

        return nums

