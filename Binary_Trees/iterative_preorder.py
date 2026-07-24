#https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # if not root:
        #     return []
        
        # ans=[]

        # ans.append(root.val)
        # ans+=self.preorderTraversal(root.left)
        # ans+=self.preorderTraversal(root.right)

        # return ans

        if not root:
            return []
        
        stack=[root]

        final=[]

        while stack:
            node=stack.pop()
            final.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return final
