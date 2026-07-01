#https://leetcode.com/problems/permutations/description/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def solve(nums,perm=[],final=[]):
            if not nums:
                final.append(perm[::])

            for i in range(len(nums)):
                new = nums[:i]+nums[i+1:]
                perm.append(nums[i])
                solve(new,perm ,final)
                perm.pop()
            return final


        return solve(nums)