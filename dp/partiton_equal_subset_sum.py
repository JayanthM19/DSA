#https://leetcode.com/problems/partition-equal-subset-sum/description/


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        
        target = sum(nums)//2
        n=len(nums)
        dp = [False]*(target+1)

        dp[0]=True

        if nums[0]<=target:
            dp[nums[0]]=True
        
        for i in range(1,n):
            
            curr = [False]*(target+1)
            curr[0]=True

            for j in range(1,target+1):

                notTaken = dp[j]

                Taken = False
                if nums[i]<=j:
                    Taken = dp[j-nums[i]]
                
                curr[j]= Taken or notTaken

            dp = curr
        
        return dp[target]

        
