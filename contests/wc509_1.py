#https://leetcode.com/contest/weekly-contest-509/problems/sum-of-integers-with-maximum-digit-range/
class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ranges=[]
        
        max_range=-1
        for num in nums:
            large=0
            small=9
            temp=num
            while temp>0:
                rem=temp%10
                large=max(large,rem)
                small=min(small,rem)
                temp//=10

            diff=large-small
            ranges.append(diff)
            max_range=max(max_range,diff)

        ans=0
        for i in range(len(nums)):
            if ranges[i]==max_range:
                ans+=nums[i]

        return ans
            
        
                