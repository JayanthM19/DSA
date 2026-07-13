#https://leetcode.com/problems/rearrange-array-elements-by-sign/
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums1=[]
        nums2=[]

        for i in range(n):
            if nums[i]>0:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])

        res=[]

        for i in range(n//2):
            res.append(nums1[i])
            res.append(nums2[i])
        
        return res