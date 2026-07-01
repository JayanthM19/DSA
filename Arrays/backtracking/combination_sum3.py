#https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums=[1,2,3,4,5,6,7,8,9]

        res=[]
        final=[]
        
        def solve(i,k,target,res,final):
            if k==len(res) and target==0:
                final.append(res[:])
                return

            
            
            if i==len(nums) or len(res)>k:
                return 
            
            if target>=nums[i]:
                res.append(nums[i])
                solve(i+1,k,target-nums[i],res,final)
                res.pop(len(res)-1)
            
            solve(i+1,k,target,res,final)
            
            

        solve(0,k,n,res,final)

        return final