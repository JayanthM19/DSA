#https://leetcode.com/problems/maximum-valid-pair-sum/
class Solution(object):
    def maxValidPairSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        best = nums[0]
        ans = 0

        for j in range(k, n):

            best = max(best, nums[j-k])

            ans = max(ans, best + nums[j])

        return ans