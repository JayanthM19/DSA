#https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        final=[]
        if not root:
            return []
        
        final+=self.postorderTraversal(root.left)
        final+=self.postorderTraversal(root.right)
        final.append(root.val)

        return final