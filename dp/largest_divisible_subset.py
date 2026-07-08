#https://leetcode.com/problems/largest-divisible-subset/
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()

        n=len(nums)

        dp=[1]*n
        parent = [0]*n
        for i in range(n):
            parent[i]=i
        
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]= dp[j]+1
                    parent[i]=j

        idx=dp.index(max(dp))

        ans=[]

        while parent[idx]!=idx:
            ans.append(nums[idx])
            idx=parent[idx]

        ans.append(nums[idx])

        return ans[::-1]


