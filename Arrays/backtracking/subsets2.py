#https://leetcode.com/problems/subsets-ii/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        final=[]

        def solve(nums,i,res,final):
            if i==len(nums):
                final.append(res[:])
                return
            
            res.append(nums[i])
            solve(nums,i+1,res,final)
            
            res.pop(len(res)-1)

            idx=i+1
            while idx<len(nums) and nums[idx]==nums[i]:
                idx+=1
            
            solve(nums,idx,res,final)

        solve(nums,0,res,final)

        return final