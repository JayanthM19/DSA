#https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        if not head.next:
            return head

        temp=head
        
        while temp and temp.next:
            temp.val,temp.next.val=temp.next.val,temp.val
            temp=temp.next.next
        
        return head
            

