#https://leetcode.com/problems/longest-mountain-in-array/
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)

        up,down=[1]*n,[1]*n

        for i in range(1,n):
            if arr[i-1]<arr[i]:
                up[i]=1+up[i-1]
        
        for j in range(n-2,-1,-1):
            if arr[j]>arr[j+1]:
                down[j]=1+down[j+1]
        
        ans=0
        for i in range(n):
            if up[i]>1 and down[i]>1:

                ans=max(ans,up[i]+down[i]-1)

        return ans


        
