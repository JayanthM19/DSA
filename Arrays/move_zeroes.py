#https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k,count=0,0
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
                count+=1
 
        while count!=n:
            nums[count]=0
            count+=1
        
        


