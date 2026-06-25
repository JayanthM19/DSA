#https://leetcode.com/problems/count-subarrays-with-majority-element-i/description/

class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        final=0

        for l in range(n):
            target_count=0
            for r in range(l,n):
    

                length=r-l+1

                if nums[r]==target:
                    target_count+=1
                
                if target_count>length//2:
                    final+=1
        
        return final


