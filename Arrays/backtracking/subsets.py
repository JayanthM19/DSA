#https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n=len(nums)
        res=[]
        final=[]
        def solve(nums,index,res,final):
            if index==n:
                final.append(res[::])
                return

            res.append(nums[index])
            solve(nums,index+1,res,final)
            res.pop(len(res)-1)
            solve(nums,index+1,res,final)



        solve(nums,0,res,final)
        return final
