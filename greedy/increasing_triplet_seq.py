#https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)

        # dp=[1]*n

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i]>nums[j]:

        #             dp[i]=max(dp[i],dp[j]+1)

        # return max(dp)>=3

        first,second = float('inf'),float('inf')

        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False

        