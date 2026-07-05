#https://leetcode.com/problems/unique-middle-element/
class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k=(len(nums)//2)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        for key,val in freq.items():
            if key==nums[k]:
                if val==1:
                    return True

        return False