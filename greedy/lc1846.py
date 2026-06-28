#https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        arr.sort()
        
        arr[0]=1

        n=len(arr)

        for i in range(n-1):
            if arr[i+1]>arr[i]+1:
                
                arr[i+1]=arr[i]+1

        return arr[n-1]


        