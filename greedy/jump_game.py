#https://leetcode.com/problems/jump-game/description/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        # def solve(i):
        #     if i==n-1:
        #         return True
            
        #     if nums[i]==0:
        #         return False
            
        #     for jump in range(1,nums[i]+1):

        #         if jump<n and solve(i+jump):
        #             return True
                
        #     return False

        #return solve(0)

#Memoization

        # dp=[-1]*(n)
        # def solve(ind):
        #     if ind==n-1:
        #         return True

        #     if nums[ind]==0:
        #         return False

        #     if dp[ind]!=-1:
        #         return dp[ind]
            
        #     for jump in range(1,nums[ind]+1):

        #         if solve(jump+ind):
        #             dp[ind]=True
        #             return True

        #     dp[ind]=False
        #     return False
        # return solve(0)


#Tabulation

        # dp=[False]*n
        # dp[n-1]=True

        # for i in range(n-2,-1,-1):
            
        #     for jump in range(1,nums[i]+1):

        #         if i+jump<n and dp[i+jump]:
        #             return True
        #             break
        
        # return dp[0]


#Greedy(optimal)

        goal=n-1

        for i in range(n-2,-1,-1):

            if i+nums[i]>=goal:
                goal=i
        
        return goal==0