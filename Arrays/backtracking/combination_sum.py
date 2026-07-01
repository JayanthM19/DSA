#https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        final=[]
        
        def solve(i,target,res,final):
            if target==0:
                final.append(res[:])
                return
            
            if i==len(candidates):
                return

            if candidates[i]<=target:

                res.append(candidates[i])
                solve(i,target-candidates[i],res,final)
                res.pop()
            
            solve(i+1,target,res,final)


        solve(0,target,res,final)
        return final