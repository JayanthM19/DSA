#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Kadanes algo
        total=0
        maxi=float('-inf')

        for num in nums:
            total+=num
            maxi=max(total,maxi)
            if total<0:
                total=0
        
        return maxi