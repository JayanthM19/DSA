#https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        ans=0
        i=0

        while i<n:
            curr=0

            while i<n and nums[i]:
                curr+=1
                i+=1
            ans=max(ans,curr)
            
            i+=1

        return ans

       