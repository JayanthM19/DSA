#https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        perm=[]
        final=[]
        def solve(nums):
            if not nums:
                final.append(perm[:])
                
            for i in range(len(nums)):

                if i>0 and nums[i]==nums[i-1]:
                    continue
                
                nextnums=nums[:i]+nums[i+1:]
                perm.append(nums[i])
                solve(nextnums)
                perm.pop()

            
                
            

        solve(nums)

        return final