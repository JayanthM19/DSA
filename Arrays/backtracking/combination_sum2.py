#https://leetcode.com/problems/combination-sum-ii/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()

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
                solve(i+1,target-candidates[i],res,final)
                res.pop()

            idx=i+1
            while idx<len(candidates) and candidates[idx]==candidates[i]:
                idx+=1
            
            solve(idx,target,res,final)

        solve(0,target,res,final)

        return final