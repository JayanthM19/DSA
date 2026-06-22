#https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
#Recursion
        # def solve(i):
        #     if i==n-1:
        #         return 0
            
        #     ans=float('inf')
        #     for jump in range(1,nums[i]+1):
        #         ans=min(ans,1+solve(jump+i))
            
        #     return ans
        # return solve(0)

#Memoization

        # dp={}
        # def solve(ind):

        #     if ind==n-1:
        #         return 0
            
        #     if ind in dp:
        #         return dp[ind]

        #     ans=float('inf')
        #     for jump in range(1,nums[ind]+1):
        #         ans=min(ans,1+solve(ind+jump))

        #         dp[ind]=ans
        #     return ans
        # return solve(0)
        
#Greedy


        jumps,curr,far=0,0,0

        for i in range(n-1):

            far=max(far,i+nums[i])

            if i==curr:
                jumps+=1

                curr = far
        
        return jumps
