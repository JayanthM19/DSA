#https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        final=[]

        final.append(root.val)

        for child in root.children:
            final+=self.preorder(child)

        return final